import os
from telebot.types import ReplyKeyboardMarkup

# Telegram bot token from BotFather
TELEBOT_TOKEN = os.getenv('TELEBOT_TOKEN')

# Shell query for get validators state data
VALIDATOR_QUERY = os.getenv('VALIDATOR_QUERY', 'cyberdcli query staking validators --trust-node=true')

# Development mode for easy bot stop
DEV_MODE = os.getenv('DEV_MODE', 0)

# SQLLite file name
DB_FILE = os.getenv('DB_FILE', 'db_sqlite.vdb')

# Hourly notifications
SCHEDULER_TIME = 60 * 60

# BASE MENU
BASE_MENU = ['Add validator moniker', 'Jail check', 'Hourly jail check', 'Validator list', 'Reset validator moniker']
BASE_MENU_LOWER = list(map(str.lower, BASE_MENU))
BASE_KEYBOARD = ReplyKeyboardMarkup(True, True)
BASE_KEYBOARD.add(BASE_MENU[0], BASE_MENU[4])
BASE_KEYBOARD.add(BASE_MENU[1], BASE_MENU[2])
BASE_KEYBOARD.add(BASE_MENU[3])
