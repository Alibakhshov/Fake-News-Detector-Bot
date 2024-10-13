import telebot
from config import BOT_TOKEN
from commands.start import start_command
from commands.predict import predict_command
from commands.help import help_command
from commands.about import about_command
from commands.statistics import statistics_command
from logging_config import setup_logging

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

@bot.message_handler(commands=['statistics'])
def handle_statistics(message):
    statistics_command(bot, message)

# Start polling for messages
if __name__ == "__main__":

    print("Bot is running...")
    print("Press Ctrl + C to stop the bot.")
    
    bot.polling(none_stop=True)
