from flask import Flask, render_template, session, request, redirect, url_for
from forms import LoginForm, RegistrationForm, SearchForm
import requests
from sql import close_database
from users import perform_login, perform_registration, check_login_status

app = Flask(__name__) #application name

app.config['SECRET_KEY'] = '5791628bb' # Sets a secret key

@app.route('/')
def home():
    login = check_login_status(session)
    return render_template('index.html', login=login)

@app.route('/search', methods=['GET', 'POST'])
def search():
    login = check_login_status(session)
    # Prepare animal-search form
    form = SearchForm()
    animals = ''
    error_msg = ''
    apiKey = 'bFfXUXiyWRCflQSBUyLSHC8la0ZZCrx9WCIrPcBuU91WsJIM14'
    secret = 'vXenHeaPS3MKgbb6D7QIpdryvZszjRnuicrrHe9B'
    if request.method == 'POST':
        breed = request.form['breed']
        zip = request.form['zip']
        gender = request.form['gender']
        api_url = "https://api.petfinder.com/v2/oauth2/token"        
        params = {'grant_type': 'client_credentials', 'client_id': apiKey, 'client_secret': secret}
        response = requests.post(api_url, json=params)
        token = response.json()
        access_token = token["access_token"]
        headers = {"Authorization": f"Bearer {access_token}"}
        apiURL = f'https://api.petfinder.com/v2/animals?type={breed}&location={zip}&gender={gender}&limit=5'
        response = requests.get(apiURL, headers=headers)
        animals = response.json()['animals']  
        
    return render_template('search.html', form=form, login=login, error_msg=error_msg, animals=animals)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        error_msg = perform_registration(username, email, password, confirm_password)
        if error_msg:
            return render_template('register.html', username=username, email=email, error_msg=error_msg, form=form)   
        else:
            session['username'] = username
            return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error_msg = perform_login(username, password)
        if error_msg:
            return render_template('login.html', username=username, error_msg=error_msg, form=form)   
        else:
            session['username'] = username
            return redirect(url_for('home'))

    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    del session['username']
    return redirect(url_for('home'))

# Close database when app context is removed
@app.teardown_appcontext
def teardown(exception):
    close_database()