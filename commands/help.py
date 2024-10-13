def help_command(bot, message):
    help_text = (
        "This bot helps you identify if a news article is fake or real. "
        "Use /predict to submit a news article for prediction."
    )
    bot.send_message(message.chat.id, help_text)
