from model_handler import predict_news
from utils import preprocess_text
from datetime import datetime
import time

def predict_command(bot, message):
    bot.send_message(message.chat.id, "Please send the news article text for prediction.")
    
    @bot.message_handler(func=lambda msg: True)
    def handle_text(msg):
        news_text = preprocess_text(msg.text)

        # Notify the user that the prediction is being processed
        processing_message = bot.send_message(msg.chat.id, "Processing the news article... Please wait a moment.")

        # Optionally add a small delay to simulate processing time (can be adjusted)
        time.sleep(2)

        # Run the prediction (this might take some time)
        prediction = predict_news(news_text, news_url="https://reuters.com", publication_date=datetime(2024, 10, 20))

        # Delete the "Processing..." message after the prediction is ready
        bot.delete_message(chat_id=msg.chat.id, message_id=processing_message.message_id)

        # Send the final result
        bot.send_message(msg.chat.id, f"{prediction}", parse_mode="HTML")
