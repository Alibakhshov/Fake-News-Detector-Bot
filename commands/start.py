def start_command(bot, message):
    welcome_message = (
        "Welcome to the Fake/Real News Detector Bot! "
        "Use /predict to check if a news article is fake or real."
    )
    bot.send_message(message.chat.id, welcome_message)
