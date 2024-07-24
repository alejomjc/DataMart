import pyrebase
import firebase_admin
import os

from dotenv import load_dotenv
from firebase_admin import credentials, auth


load_dotenv()

firebaseConfig = {
  "apiKey": os.getenv('FIREBASE_API_KEY'),
  "authDomain": os.getenv('FIREBASE_AUTH_DOMAIN'),
  "projectId": os.getenv('FIREBASE_PROJECT_ID'),
  "storageBucket": os.getenv('FIREBASE_STORAGE_BUCKET'),
  "messagingSenderId": os.getenv('FIREBASE_MESSAGING_SENDER_ID'),
  "appId": os.getenv('FIREBASE_APP_ID'),
  "measurementId": os.getenv('FIREBASE_MEASUREMENT_ID'),
  "databaseURL": os.getenv('FIREBASE_DATABASE_URL')
}

service_account_info = {
  "type": os.getenv('FIREBASE_TYPE'),
  "project_id": os.getenv('FIREBASE_PROJECT_ID'),
  "private_key_id": os.getenv('FIREBASE_PRIVATE_KEY_ID'),
  "private_key": os.getenv('FIREBASE_PRIVATE_KEY').replace('\\n', '\n'),
  "client_email": os.getenv('FIREBASE_CLIENT_EMAIL'),
  "client_id": os.getenv('FIREBASE_CLIENT_ID'),
  "auth_uri": os.getenv('FIREBASE_AUTH_URI'),
  "token_uri": os.getenv('FIREBASE_TOKEN_URI'),
  "auth_provider_x509_cert_url": os.getenv('FIREBASE_AUTH_PROVIDER_X509_CERT_URL'),
  "client_x509_cert_url": os.getenv('FIREBASE_CLIENT_X509_CERT_URL')
}

firebase = pyrebase.initialize_app(firebaseConfig)
firebase_auth = firebase.auth()

cred = credentials.Certificate(service_account_info)
firebase_admin.initialize_app(cred)


def verify_token_local(token):
    return auth.verify_id_token(token)
