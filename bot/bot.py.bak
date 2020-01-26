#!/usr/bin/env python3
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)
import config
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def echo(update, context):
    logger.info(f'{update.message.date} - Chat: {update.message.chat_id} User: {update.message.from_user} Message: {update.message.text}')
    update.message.reply_text(update.message.text)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def help(update, context):
    update.message.reply_text('Help')

# def debug(update, context):
#     logger.info(update)

def test(update, context):
    data = dir(update.message)
    data = f'chat_id - {update.message.chat_id}, date - {update.message.date}, from_user - {update.message.from_user}'
    context.bot.send_message(chat_id=update.effective_chat.id, text=data)

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    updater = Updater(config.TOKEN, use_context=True, request_kwargs=config.REQUEST_KWARGS)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.regex('test'), test))
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()

