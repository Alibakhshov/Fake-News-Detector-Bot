import logging
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Bot Token
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Ensure the logs directory exists
LOG_DIR = 'logs'
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Logging configuration
LOG_FILE = os.path.join(LOG_DIR, 'bot.log')
logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
