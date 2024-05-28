import pickle
import requests
import tempfile
import os
from dotenv import load_dotenv

load_dotenv()

MODEL_URL = os.getenv('MODEL_URL')

def load_pickle_model(url):
    response = requests.get(url)
    response.raise_for_status()  
    with tempfile.NamedTemporaryFile(delete=True) as tmp:
        tmp.write(response.content)
        tmp.flush()
        tmp.seek(0)
        model = pickle.load(tmp)
    return model

model = load_pickle_model(MODEL_URL)