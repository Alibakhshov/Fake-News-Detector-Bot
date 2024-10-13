import logging
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Bot Token
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Logging configuration
LOG_FILE = 'logs/bot.log'
logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
