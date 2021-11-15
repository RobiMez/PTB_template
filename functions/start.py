"""Start message"""

import telegram

from decorators import typing

@typing
def start(update, context):
    """
        Send a message when the command /start is issued.
    """
    # Send welcome message
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=(
            'Hi there , im alive.\n'
            ),
        parse_mode=telegram.ParseMode.HTML,disable_web_page_preview=True)

