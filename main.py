# pylint: disable=fixme

"""
    Main execution script.
"""

# Standard imports
import os
import logging

from logging import handlers

# 3rd party imports
from telegram.ext import CommandHandler
# local imports

from functions.start import start
from functions.constants import updater, dpr


# Logging configuration

# Make folder called logs if not exists
if not os.path.exists('logs'):
    os.mkdir('logs')
# Timed log handler that rotates the
# log file by each midnight
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(name)s | %(levelname)s | %(funcName)s:%(lineno)d | %(message)s",
    handlers=[
        handlers.TimedRotatingFileHandler(
            './logs/debug.log', encoding='utf-8', when='midnight'),
        logging.StreamHandler()
    ]
)


def main():
    "Main Execution"
    # start handler
    dpr.add_handler(CommandHandler('start', start))

    updater.start_polling()
    logging.info(f'🟩  Bot is LIVE 🟩')
    updater.idle()


if __name__ == '__main__':
    main()
