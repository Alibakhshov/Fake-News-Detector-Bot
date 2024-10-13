def help_command(bot, message):
    help_text = (
        "🔹 *Available Commands:*\n\n"
        "This bot helps you identify if a news article is fake or real. "
        "Use the commands below to interact with the bot:\n\n"
        "🏠 /start - Start the bot and get a welcome message.\n"
        "💬 /predict - Submit a news article for fake/real prediction.\n"
        "ℹ️ /about - Learn more about how the bot works and the model behind it.\n"
        "🆘 /help - Display this help message.\n"
        "📊 /statistics - View statistics about the predictions made so far.\n"
    )
    bot.send_message(message.chat.id, help_text, parse_mode="Markdown")
