from model_handler import predict_news
from utils import preprocess_text

def predict_command(bot, message):
    bot.send_message(message.chat.id, "Please send the news article text for prediction.")
    
    @bot.message_handler(func=lambda msg: True)
    def handle_text(msg):
        news_text = preprocess_text(msg.text)
        prediction = predict_news(news_text)
        bot.send_message(msg.chat.id, f"The news article is: {prediction}")
