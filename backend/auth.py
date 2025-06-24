import pyrebase
import json
import os
# with open("configs/firebase_web_config.json") as f:
#   firebase_config = json.load(f)
firebase_config = json.loads(os.environ["FIREBASE_CONFIG"])

firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()

def login_user(email, password):
    try:
        return auth.sign_in_with_email_and_password(email, password)
    except:
        return None

def signup_user(email, password):
    try:
        return auth.create_user_with_email_and_password(email, password)
    except:
        return None
