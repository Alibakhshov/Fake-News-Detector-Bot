# 📰 Fake News Detector Telegram Bot

This project is a **Telegram bot** that helps users determine whether a news article is fake or real using a machine learning model trained on fake and real news articles. The bot provides commands for prediction, information about the model, help, and more. It also sends users visual insights, such as confusion matrices and classification reports, to explain the model's performance.

## 📋 Table of Contents
1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Running the Bot](#running-the-bot)
6. [Bot Commands](#bot-commands)
7. [Project Structure](#project-structure)
8. [Team](#team)
9. [Contributing](#contributing)
10. [License](#license)

## Features
- Predict whether a news article is real or fake using a logistic regression model.
- View detailed statistics, confusion matrix, classification report, and dataset distribution.
- Receive training data used for model creation.
- Clean, modular, and scalable code.
- Robust logging and error handling.
- Friendly inline buttons for quick navigation.

---

## 🛠 Prerequisites
Before running the project, ensure you have the following installed:
- **Python 3.8+**
- **pip** (Python package manager)
- A **Telegram Bot Token** from [BotFather](https://core.telegram.org/bots#botfather)

---

## 🖥️ Installation

### Step 1: Clone the Repository
Clone the project repository to your local machine:
```bash
git clone https://github.com/your-username/fake-news-detector-bot.git
cd fake-news-detector-bot
```

### Step 2: Create and Activate a Virtual Environment
It's recommended to use a virtual environment for Python projects. To create and activate one, run the following commands:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
After activating the virtual environment, install the required Python packages using `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Step 4: Create the `.env` File
Create a `.env` file in the root directory to store your sensitive configuration information like the Telegram Bot Token:

1. Create a file called `.env`:
   ```bash
   touch .env
   ```

2. Open the `.env` file and place your bot token inside as follows:
   ```
   BOT_TOKEN=your-telegram-bot-token-here
   ```

---

## ⚙️ Configuration

The project reads the bot token from the `.env` file. Ensure the token is placed there correctly.

Additionally, ensure that the required files are in the correct directories:
- **Model and Vectorizer**: Ensure that the logistic regression model and TF-IDF vectorizer are in the root directory.
- **CSV Training Data**: Ensure the file `fake_and_real_news.csv` is located at `models/data/fake_and_real_news.csv`.

---

## 🚀 Running the Bot

### Step 1: Start the Bot
Once everything is set up, run the following command to start the bot:
```bash
python bot.py
```

The bot will start polling and be ready to receive commands on Telegram.

### Step 2: Interacting with the Bot
- Open Telegram and search for your bot by its username.
- Type `/start` to begin interacting with the bot.

---

## 🤖 Bot Commands

Here’s a list of commands the bot supports:
- **/start**: Welcome message and introduction.
- **/predict**: Paste a news article, and the bot will predict whether it is fake or real.
- **/help**: Lists available commands and provides usage instructions.
- **/about**: Detailed information about the bot’s machine learning model and training process.
- **/statistics**: Displays general statistics about the bot's performance.
- **Inline buttons**: Access visual insights (e.g., confusion matrix, classification report) via inline buttons.

---

## 🗂️ Project Structure

```
fake-news-detector-bot/
│
├── bot.py                  
├── model_handler.py          
├── utils.py                  
├── config.py                 
├── logging_config.py         
├── requirements.txt          
├── .env                      
├── models/                   
│   └── data/
│       └── fake_and_real_news.csv
├── images/(confusion matrix, classification report, etc.)
└── commands/                
    ├── start.py              
    ├── predict.py           
    ├── help.py              
    ├── about.py              
    └── statistics.py         
```

---

## Team
This project was developed by the following team members:

<!-- Adding names with link to their Github -->


Feel free to contact us for any questions or issues related to this project.

---

## Contributing

Contributions are welcome! If you would like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a pull request explaining your changes.

All contributions will be reviewed, and feedback will be provided if necessary.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

### Notes
- **Modular Code**: The project is structured in a modular way. Each command and functionality is separated into different files for better maintainability and scalability.
- **Logging**: The bot uses logging to track errors and important events. Logs are stored in `logs/bot.log`.
- **Visual Insights**: The bot provides visualizations such as confusion matrix, classification report, and dataset distribution via inline buttons.
