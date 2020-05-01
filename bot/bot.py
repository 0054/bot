#!/usr/bin/env python3
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove, Update)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler, CallbackContext)
import config
import telegram
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


# middleware

def loggerInfo(f):
    def wrap(update: Update, context: CallbackContext):
        # logger.info(f'{update.message.date} - Chat: {update.message.chat_id} User: {update.message.from_user} Message: {update.message.text}')
        f(update, context)
    return wrap

#handlers
@loggerInfo
def echo(update, context):
    update.message.reply_text(update.message.text)


@loggerInfo
def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

@loggerInfo
def getID(update: Update, context: CallbackContext):
    userID = update.message.from_user.id
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'Your ID = {userID}')

# def botAddedToChat(update: Update, context: CallbackContext):
#     for memder in update.mem

def getChatID(update: Update, context: CallbackContext):
    chatID = update.effective_chat.id
    context.bot.send_message(chat_id=chatID, text=f'chat id = {chatID}')

def debug(update: Update, context: CallbackContext):
    updateDir = dir(update)
    updateData = update
    contextDir = dir(context.chat_data)
    contextData = context.chat_data()
    # resultData = f'updateDir: {updateDir},\n\nupdateData: {updateData}'
    resultData = f'context: {contextDir},\n\ncontextData: {contextData}'
    context.bot.send_message(chat_id=update.effective_chat.id, text=resultData)


@loggerInfo
def test(update: Update, context: CallbackContext):
    data = dir(update.message)
    data = f'chat_id - {update.message.chat_id}, date - {update.message.date}, from_user - {update.message.from_user}'
    context.bot.send_message(chat_id=update.effective_chat.id, text=data)


@loggerInfo
def error(update: Update, context: CallbackContext):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater(config.TOKEN, use_context=True, request_kwargs=config.REQUEST_KWARGS)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("getID", getID))
    dp.add_handler(CommandHandler("help", help))

    dp.add_handler(MessageHandler(Filters.regex('test'), test))
    dp.add_handler(MessageHandler(Filters.regex('debug'), debug))
    dp.add_handler(MessageHandler(Filters.update.channel_post & Filters.command, getChatID))
    dp.add_handler(MessageHandler(Filters.all, saveUpdate))
    dp.add_handler(MessageHandler(Filters.private, echo))

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

