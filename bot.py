import telebot
from config import BOT_TOKEN
from commands.start import start_command
from commands.predict import predict_command
from commands.help import help_command
from commands.about import about_command
from commands.statistics import statistics_command
from logging_config import setup_logging
import time

# Set up logging
setup_logging()

# Initialize the bot
bot = telebot.TeleBot(BOT_TOKEN)

# Handlers for commands
@bot.message_handler(commands=['start'])
def handle_start(message):
    start_command(bot, message)

@bot.message_handler(commands=['predict'])
def handle_predict(message):
    predict_command(bot, message)

@bot.message_handler(commands=['help'])
def handle_help(message):
    help_command(bot, message)

@bot.message_handler(commands=['about'])
def handle_about(message):
    about_command(bot, message)

# Handler for button clicks in /about command
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "confusion_matrix":
        # Send confusion matrix image
        bot.send_photo(call.message.chat.id, open('images/confusion_matrix.png', 'rb'))
    elif call.data == "classification_report":
        # Send classification report image
        bot.send_photo(call.message.chat.id, open('images/classification_report.png', 'rb'))
    elif call.data == "dataset_distribution":
        # Send dataset distribution image
        bot.send_photo(call.message.chat.id, open('images/dataset_distribution.png', 'rb'))
    elif call.data == "training_data":
        # Step 1: Send the "wait a bit" message
        wait_message = bot.send_message(call.message.chat.id, "⏳ Wait a bit while we are sending the data...")

        # Step 2: Use chat action to indicate that the bot is uploading the file
        bot.send_chat_action(call.message.chat.id, 'upload_document')

        # Step 3: Simulate a small delay (optional) to enhance UX
        time.sleep(2)  # You can adjust the sleep time as needed

        # Step 4: Send the training data CSV file
        bot.send_document(call.message.chat.id, open('models/data/fake_and_real_news.csv', 'rb'))

        # Step 5: Delete the "wait a bit" message
        bot.delete_message(call.message.chat.id, wait_message.message_id)

@bot.message_handler(commands=['statistics'])
def handle_statistics(message):
    statistics_command(bot, message)

# Start polling for messages
if __name__ == "__main__":

    print("Bot is running...")
    print("Press Ctrl + C to stop the bot.")
    
    bot.polling(none_stop=True)
