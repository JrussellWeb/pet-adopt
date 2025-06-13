from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, InputRequired

class RegistrationForm(FlaskForm):
    username = StringField('Username: ',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email: ',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password: ', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password: ', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username = StringField('Username: ',
                        validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password: ', validators=[DataRequired()])
    submit = SubmitField('Login')

class SearchForm(FlaskForm):
    breed = SelectField('Breed: ',
                           choices=[('dog', 'Dog'), ('cat', 'Cat'), ('rabbit', 'Rabbit')])
    zip = StringField('Zip Code: ',
                        validators=[InputRequired()])
    gender = SelectField('Gender: ',
                        choices=[('male', 'Boy'), ('female', 'Girl')])
    
    submit = SubmitField('Search')