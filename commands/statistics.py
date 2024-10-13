def statistics_command(bot, message):
    stats_text = (
        "The bot has made X predictions so far, with Y% real and Z% fake predictions."
    )
    bot.send_message(message.chat.id, stats_text)
