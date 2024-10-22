# model_handler.py

import pickle
import logging
from sklearn.exceptions import NotFittedError
from sklearn.feature_extraction.text import TfidfVectorizer
import os

# Load the trained model and vectorizer
with open('models/logistic_regression_model_trained.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('models/tfidf_vectorizer.pkl', 'rb') as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

import os
from transformers import pipeline

from transformers import pipeline

# Use a publicly available model for text classification
classifier = pipeline(
    "text-classification", 
    model="distilbert-base-uncased-finetuned-sst-2-english"  # Replace with a valid model
)

def interpret_confidence(confidence):
    """Interpret the confidence level into a human-readable format."""
    if confidence > 0.9:
        return "High confidence"
    elif 0.6 <= confidence <= 0.9:
        return "Medium confidence"
    else:
        return "Low confidence"

def predict_news(text):
    """Predict if the news is real or fake using a Hugging Face model."""
    try:
        # Get the prediction and confidence
        prediction = classifier(text)
        label = prediction[0]['label']
        confidence = prediction[0]['score']

        # Convert label to readable form
        prediction_label = "Real" if label == "POSITIVE" else "Fake"

        # Interpret confidence level
        confidence_level = interpret_confidence(confidence)

        # Shorten the news article text for display (first 50 characters)
        snippet = text[:50] + "..." if len(text) > 50 else text

        # Add visual elements for Real/Fake
        icon = "✅" if prediction_label == "Real" else "❌"

        # Format the message using HTML and newlines (\n)
        message = (
            f"📰 <b>News Article Analysis</b> 📰\n\n"
            f"<b>Snippet:</b> {snippet}\n"
            f"<b>Prediction:</b> {icon} The news article is predicted to be: <b>{prediction_label}</b>\n"
            f"<b>Confidence:</b> {confidence:.2f} ({confidence_level})\n\n"
            f"⚠️ This is a machine learning model's prediction and should be used with caution!"
        )
        return message
    except Exception as e:
        return f"Error during prediction: {e}"
