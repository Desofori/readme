import os
import pyotp
import bcrypt

user_keys = {}
user_secrets = {}
user_passwords = {}

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def check_password(stored_password, provided_password):
    return bcrypt.checkpw(provided_password.encode(), stored_password)

def generate_user_key(username):
    key = os.urandom(32)
    user_keys[username] = key
    return key

def store_user_password(username, password):
    user_passwords[username] = hash_password(password)

def generate_user_secret(username):
    secret = pyotp.random_base32()
    user_secrets[username] = secret
    return secret

def get_user_key(username):
    return user_keys.get(username)

def get_user_secret(username):
    return user_secrets.get(username)

def authenticate_user(username, password, totp):
    if username not in user_passwords or not check_password(user_passwords[username], password):
        return False

    secret = get_user_secret(username)
    if not pyotp.TOTP(secret).verify(totp):
        return False

    return True
