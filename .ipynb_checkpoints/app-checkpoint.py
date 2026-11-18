import joblib
import numpy as np
from preprocessor import process_review
from flask import Flask, request, jsonify

app = Flask(__name__)

model = joblib.load('model.joblib')
vectorizer = joblib.load('vectorizer.joblib')

@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    reviews = data['reviews']

    process_rev = process_review(reviews)
    
    process_rev = vectorizer.transform([process_rev])

    prediction = model.predict(process_rev)

    return jsonify({"prediction": "positive" if prediction[0] == "1" else "negative"})


@app.route("/health", methods = ['GET'])
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":

    import os 
    app.run(host="127.0.0.1" , port=int(os.environ.get("PORT", 5000)))
                    