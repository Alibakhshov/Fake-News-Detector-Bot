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

import re
from datetime import datetime
from textblob import TextBlob
from transformers import pipeline

from transformers import pipeline
from textblob import TextBlob
from datetime import datetime

# Load models (classifier and summarizer)
classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Example of trusted sources
trusted_sources = ["reuters.com", "bbc.com", "cnn.com"]

def interpret_confidence(confidence):
    """Interpret the confidence level into a human-readable format."""
    if confidence > 0.9:
        return "High confidence"
    elif 0.6 <= confidence <= 0.9:
        return "Medium confidence"
    else:
        return "Low confidence"

def get_sentiment(text):
    """Analyze sentiment of the news article (positive, neutral, or negative)."""
    analysis = TextBlob(text)
    sentiment_score = analysis.sentiment.polarity

    if sentiment_score > 0:
        return "Positive"
    elif sentiment_score == 0:
        return "Neutral"
    else:
        return "Negative"

def check_news_source(url):
    """Check the credibility of the news source."""
    if any(source in url for source in trusted_sources):
        return "Trusted Source"
    else:
        return "Unknown or Less Trusted Source"

def is_recent(publication_date):
    """Check if the article is recent (within the last 7 days)."""
    now = datetime.now()
    return (now - publication_date).days <= 7

def classify_topic(text):
    """Classify the topic of the news article (e.g., Politics, Health, Technology)."""
    keywords = {
        "Politics": ["election", "government", "policy"],
        "Health": ["vaccine", "COVID", "medicine"],
        "Technology": ["AI", "blockchain", "software"],
        "Economy": ["market", "economy", "stocks"]
    }

    for topic, words in keywords.items():
        if any(word.lower() in text.lower() for word in words):
            return topic
    return "General"

def summarize_article(text):
    """Summarize the article if it's too long using a pre-trained summarizer."""
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
    return summary

def chunk_text(text, chunk_size=350):
    """Split the text into chunks of `chunk_size` words."""
    words = text.split()
    return [' '.join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]

def predict_news(text, news_url=None, publication_date=None):
    """Predict if the news is real or fake, and handle long articles."""
    try:
        # Check if the text is too long (more than 350 words)
        if len(text.split()) > 350:
            # Summarize the text if it's very long
            summarized_text = summarize_article(text)
            text = summarized_text
        
        # If the summarized text is still too long, chunk it
        chunks = chunk_text(text)

        # Initialize variables to store overall results
        predictions = []
        sentiments = []
        for chunk in chunks:
            prediction = classifier(chunk)
            label = prediction[0]['label']
            confidence = prediction[0]['score']
            predictions.append((label, confidence))
            sentiments.append(get_sentiment(chunk))

        # Aggregate predictions from all chunks
        final_label = "Real" if all(label == "POSITIVE" for label, _ in predictions) else "Fake"
        avg_confidence = sum(conf for _, conf in predictions) / len(predictions)
        final_sentiment = max(set(sentiments), key=sentiments.count)  # Majority sentiment

        # Interpret confidence level
        confidence_level = interpret_confidence(avg_confidence)

        # Shorten the news article text for display (first 50 characters)
        snippet = text[:50] + "..." if len(text) > 50 else text

        # Check the credibility of the source if a URL is provided
        source_reliability = check_news_source(news_url) if news_url else "Unknown Source"

        # Determine if the article is recent
        relevance = "Recent" if publication_date and is_recent(publication_date) else "Outdated"
        publication_info = f" (Published on {publication_date.strftime('%Y-%m-%d')})" if publication_date else ""

        # Classify the topic of the article
        topic = classify_topic(text)

        # Add visual elements for Real/Fake
        icon = "✅" if final_label == "Real" else "❌"

        # Format the message using HTML and newlines (\n)
        message = (
            f"📰 <b>News Article Analysis</b> 📰\n\n"
            f"<b>Snippet:</b> {snippet}\n"
            f"<b>Prediction:</b> {icon} The news article is predicted to be: <b>{final_label}</b>\n"
            f"<b>Confidence:</b> {avg_confidence:.2f} ({confidence_level})\n"
            f"<b>Sentiment:</b> {final_sentiment}\n"
            f"<b>Source Reliability:</b> {source_reliability}\n"
            f"<b>Relevance:</b> {relevance}{publication_info}\n"
            f"<b>Topic:</b> {topic}\n\n"
            f"⚠️ This is a machine learning model's prediction and should be used with caution!"
        )
        return message
    except Exception as e:
        return f"Error during prediction: {e}"