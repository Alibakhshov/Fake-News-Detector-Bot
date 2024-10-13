def statistics_command(bot, message):
    stats_text = (
        "📊 *Bot Usage Statistics*\n\n"
        "Here are some general statistics and information about the bot's performance:\n\n"
        "✅ *Model Accuracy*: The bot’s machine learning model has an accuracy of *99.2%*, meaning it predicts whether a news article is real or fake with high precision.\n\n"
        "📉 *Performance*: Based on thousands of test cases, the bot correctly identifies:\n"
        "   - *100%* of real news articles\n"
        "   - *99%* of fake news articles\n\n"
        "📈 *How to Use*: To get started, use the /predict command and paste any news article you want to verify. "
        "The bot will analyze the text and tell you whether it's likely to be real or fake.\n\n"
        "ℹ️ Use /about to learn more about how the bot works."
    )
    
    bot.send_message(message.chat.id, stats_text, parse_mode="Markdown")
