import pandas as pd
from flask import Flask, request, render_template, jsonify
import uuid
from datetime import datetime
import firebase_admin
from services.storeData import store_data
from services.loadModel import model

app = Flask(__name__)

FEATURES = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
LABEL = ['Iris Setosa', "Iris Versicolor", "Iris Virginica"]

@app.route('/')
def index():
    return jsonify({"status": "SUCCESS", "message": "Success connect"}), 200

@app.route('/predict', methods=["POST"])
def predict():
    try:
        args = request.args
        sl = args.get('sl', default=0.0, type=float)
        sw = args.get('sw', default=0.0, type=float)
        pl = args.get('pl', default=0.0, type=float)
        pw = args.get('pw', default=0.0, type=float)

        if sl == 0.0 and sw == 0.0 and pl == 0.0 and pw == 0.0:
            return jsonify({"status": "FAILURE", 
                            "message": "All input values are zero, which is not valid"
                            }), 400

        new_data = [[sl, sw, pl, pw]]
        new_data = pd.DataFrame(new_data, columns=FEATURES)

        res = model.predict(new_data)
        res = LABEL[res[0]]
        
        id = str(uuid.uuid4())
        createdAt = datetime.utcnow().isoformat()

        response = {
            "id": id,
            "result": res,
            "createdAt": createdAt
        }

        store_data(id, response)

        return jsonify({"status": "SUCCESS", 
                        "data": response
                        }), 200
    
    except Exception as e:
        return jsonify({"status": "ERROR", 
                        "message": f"Internal error: {str(e)}"
                        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)