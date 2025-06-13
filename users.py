from sql import get_user, insert_user

def perform_registration(username, email, password, confirm_password):
    # Make sure the user doesn't exist already
    row = get_user(username)
    if row:
        return f"User {username} already exists"
    
    # Make sure the passwords match
    if password != confirm_password:
        return "Passwords don't match"
    
    # Register the user
    insert_user(username, password, email)
    return None


def perform_login(username, password):
    # Get the user information
    row = get_user(username)
    if not row:
        return f"User {username} does not exist"
    
    db_username, db_password, db_email = row
    if password != db_password:
        return "Invalid credentials"
    
    return None

def check_login_status(session):
    if 'username' in session:
        return session['username']
    else:
        return None
