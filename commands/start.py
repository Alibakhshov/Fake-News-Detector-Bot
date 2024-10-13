def start_command(bot, message):
    user_first_name = message.from_user.first_name if message.from_user.first_name else "there"
    welcome_message = (
        f"👋 Hi *{user_first_name}*! Welcome to the *Fake/Real News Detector Bot*! 🎉\n\n"
        "I'm here to assist you in finding out if the news you're reading is *fake* or *real*. 📰✅❌\n\n"
        "All you need to do is type /predict and paste the article you'd like me to check. "
        "I’ll take care of the rest! Let's make sure you get the facts straight! 💪\n\n"
        "Feel free to ask for /help if you need any guidance!"
    )
    bot.send_message(message.chat.id, welcome_message, parse_mode="Markdown")
