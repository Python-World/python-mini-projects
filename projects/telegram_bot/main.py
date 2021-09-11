'''
    BOT FOR TELEGRAM
'''

import random
import logging
from telegram import (ParseMode)
from telegram.ext import (Updater, CommandHandler)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def error_callback(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def start(update, context):
    ''' 
        Start
    '''
    context.bot.send_message(update.message.chat_id,
                             "Welcome! to simple telegram bot", parse_mode=ParseMode.HTML)

    ''' 
        We can call other commands, without it being activated in the chat (/ help).
    '''
    coin(update, context)


def coin(update, context):
    '''
        ⚪️ / ⚫️ Currency
         Generate an elatory number between 1 and 2.
    '''
    cid = update.message.chat_id

    msg = "⚫️ face " if random.randint(1, 2) == 1 else "⚪️ cross"
    '''
        He responds directly on the channel where he has been spoken to.
    '''
    update.message.reply_text(msg)


def main():
    TOKEN = "1914536904:AAF4ZnqNvyg1pk-1pCPzTqhDYggAyf-1CF8"

    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    '''
        Events that will activate our bot.
    '''
    dp.add_handler(CommandHandler('start',	start))
    dp.add_handler(CommandHandler('coin',	coin))

    dp.add_error_handler(error_callback)

    '''
        The bot starts
    '''
    updater.start_polling()

    '''
        or leave listening. Keep it from stopping.
    '''
    updater.idle()


if __name__ == '__main__':
    print('[Telegram simple bot] Start...')
    main()