# model_handler.py

import pickle
import logging
from sklearn.exceptions import NotFittedError

# Load the trained model and vectorizer
with open('models/logistic_regression_model_trained.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('models/tfidf_vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

def predict_news(text):
    """Predict if the news is real or fake, with formatted output"""
    try:
        # Ensure the input text is valid
        if not text or not text.strip():
            return "Invalid input text"

        # Preprocess and vectorize the input text
        text_vectorized = vectorizer.transform([text])

        # Perform the prediction
        prediction = model.predict(text_vectorized)
        prediction_proba = model.predict_proba(text_vectorized)

        # Format the output
        formatted_output = f"The news article is predicted to be: **{prediction[0]}**\n"
        formatted_output += f"Model confidence: **{prediction_proba[0].max():.2f}**"

        return formatted_output
    except NotFittedError as nf_error:
        logging.error(f"Model not fitted properly: {nf_error}")
        return "Model is not trained correctly"
    except Exception as e:
        logging.error(f"Prediction error: {e}")
        return "Error during prediction"
