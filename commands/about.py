# commands/about.py

def about_command(bot, message):
    about_text = (
        "📰 *About This Bot*\n\n"
        "This bot uses a machine learning model to detect whether a news article is *real* or *fake*.\n\n"
        "💡 *How It Works*\n"
        "The model was trained on a large dataset of real and fake news articles using a technique called *logistic regression*. "
        "This technique helps classify news articles into two categories: 'Fake' or 'Real' based on the text content.\n\n"
        
        "📊 *Training Process*\n"
        "During training, the model was fed thousands of news articles labeled as either real or fake. "
        "We used a powerful text processing method called *TF-IDF* (Term Frequency-Inverse Document Frequency) "
        "to convert the raw news text into numerical values that the model can understand.\n\n"
        
        "📈 *Model Performance*\n"
        "The model achieved an impressive accuracy of *99.2%* during testing! Below are the detailed performance metrics:\n\n"
        "🔹 *Precision for Fake News*: 100%\n"
        "🔹 *Recall for Fake News*: 99%\n"
        "🔹 *Precision for Real News*: 99%\n"
        "🔹 *Recall for Real News*: 100%\n\n"
        
        "📉 *Confusion Matrix*\n"
        "The confusion matrix gives a deeper insight into how well the model performed:\n"
        "`[ 962,  11]`  Fake News: Correctly classified as Fake, Incorrectly classified as Real\n"
        "`[  4, 1003]` Real News: Incorrectly classified as Fake, Correctly classified as Real\n\n"
        
        "📚 *Dataset Used*\n"
        "The dataset contained both fake and real news articles, which were carefully labeled and used to teach the model how to distinguish between them. "
        "The dataset was split into two parts: 80% for training the model and 20% for testing how well the model performs on unseen data.\n\n"
        
        "🤖 *Why This Matters*\n"
        "With the rise of misinformation, especially online, it's important to have tools that help distinguish between truthful news and misleading information. "
        "This bot aims to make it easier for you to quickly verify the authenticity of news articles you come across.\n\n"
        
        "Feel free to use the /predict command to try it out! Simply paste a news article and see if it's real or fake."
    )
    
    bot.send_message(message.chat.id, about_text, parse_mode="Markdown")
