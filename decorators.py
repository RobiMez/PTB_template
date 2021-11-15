
from functools import wraps
from telegram import ChatAction

from functions.constants import ADMINS


def typing(func):
    """Sends typing action while processing command."""
    @wraps(func)
    def command_func(update, context, *args, **kwargs):
        context.bot.send_chat_action(
            chat_id=update.effective_message.chat_id,
            action=ChatAction.TYPING)
        return func(update, context,  *args, **kwargs)
    return command_func

def pm_only(func):
    """Limits command to only execute on DMs with the bot."""
    @wraps(func)
    def command_func(update, context, *args, **kwargs):
        if update.effective_chat['type'] == 'private':
            return func(update, context,  *args, **kwargs)
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,text='Sorry but that is a direct message only command.')
    return command_func

def ignore_non_pm(func):
    """Ignores all updates that are not from direct messages"""
    @wraps(func)
    def command_func(update, context, *args, **kwargs):
        if update.effective_chat['type'] == 'private':
            return func(update, context,  *args, **kwargs)
    return command_func

def admin_only(func):
    """Limits command to only execute when sent by valid admins."""
    @wraps(func)
    def command_func(update, context, *args, **kwargs):
        user = update.effective_user.id
        if user in ADMINS:
            return func(update, context,  *args, **kwargs)
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,text='Sorry but you dont have the privillages for that.')
    return command_func