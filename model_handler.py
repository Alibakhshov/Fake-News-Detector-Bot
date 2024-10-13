# model_handler.py

import pickle
import logging

# Load the trained model and vectorizer
with open('models/logistic_regression_model_trained.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('models/tfidf_vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

def predict_news(text):
    """Predict if the news is real or fake"""
    try:
        # Preprocess and vectorize the input text
        text_vectorized = vectorizer.transform([text])
        prediction = model.predict(text_vectorized)
        return prediction[0]
    except Exception as e:
        logging.error(f"Prediction error: {e}")
        return "Error during prediction"
