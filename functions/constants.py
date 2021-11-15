"""
    Constants

    Configures key variables and 
    Parses .env to make tokens available to the app 
"""
from logging import warn
from os import getenv
import sentry_sdk

import dotenv
import certifi

from telegram import Bot
from telegram.ext import Updater
from pymongo import MongoClient

# .env parsing
TOKEN = dotenv.get_key('.env', 'TOKEN') or getenv('TOKEN')
DBURI = dotenv.get_key('.env', 'DBURI') or getenv('DBURI')
SENTRY = dotenv.get_key('.env', 'SENTRY') or getenv('SENTRY')

if TOKEN:
    # Define bot
    bot = Bot(token=TOKEN)
    # Define updater and dispatcher
    updater = Updater(token=TOKEN, use_context=True)
    dpr = updater.dispatcher
else:
    warn('No TOKEN found in .env file or environment variable')

# Mongo db cluster definition
if DBURI:
    cluster = MongoClient(DBURI, tlsCAFile=certifi.where())
    # Mongodb collection definition
    db = cluster['test']
    # User and Post database definition
    posts_db = db['posts']
    users_db = db['users']
else:
    warn('No DBURI found in .env file or environment variable')

# Sentry configuration
if SENTRY:
    sentry_sdk.init(
        SENTRY,
        traces_sample_rate=1.0
    )
else:
    warn('No SENTRY found in .env file or environment variable')

# Admin list ( Telegram ids )
ADMINS = [ ]
