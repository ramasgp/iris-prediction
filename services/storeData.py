import firebase_admin
from firebase_admin import credentials, firestore
import os

cred_path = os.path.expanduser('~/.config/gcloud/application_default_credentials.json')
cred = credentials.ApplicationDefault()
firebase_admin.initialize_app(cred, {
    'projectId': 'iris-prediction-424604',  # Ganti dengan ID proyek Anda jika berbeda
})

db = firestore.client()

def store_data(id, data):
    predict_collection = db.collection('prediction')
    predict_collection.document(id).set(data)
