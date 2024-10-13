# commands/about.py
from telebot import types

def about_command(bot, message):
    about_text = (
        "📰 *About This Bot*\n\n"
        "This bot uses a machine learning model to detect whether a news article is *real* or *fake*.\n\n"
        "💡 *How It Works*\n\n"
        "The model was trained on a large dataset of real and fake news articles using a technique called *logistic regression*. "
        "This technique helps classify news articles into two categories: 'Fake' or 'Real' based on the text content.\n\n"
        
        "📊 *Model Performance*\n\n"
        "The model achieved an impressive accuracy of *99.2%* during testing! Use the buttons below to view key information about the model."
    )

    # Creating inline buttons
    markup = types.InlineKeyboardMarkup()
    confusion_matrix_btn = types.InlineKeyboardButton(text="📉 Confusion Matrix", callback_data="confusion_matrix")
    classification_report_btn = types.InlineKeyboardButton(text="📈 Classification Report", callback_data="classification_report")
    dataset_distribution_btn = types.InlineKeyboardButton(text="📊 Dataset Distribution", callback_data="dataset_distribution")
    training_data_btn = types.InlineKeyboardButton(text="📁 View Training Data", callback_data="training_data")

    # Adding buttons to the markup
    markup.add(confusion_matrix_btn, classification_report_btn, dataset_distribution_btn, training_data_btn)
    
    # Sending the about text with inline buttons
    bot.send_message(message.chat.id, about_text, parse_mode="Markdown", reply_markup=markup)
