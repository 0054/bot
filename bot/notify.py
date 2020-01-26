#!/usr/bin/env python3

import json
import telegram
from flask import Flask
from flask import request
from flask import jsonify
import config
from telegram.utils.request import Request
ProxyRequest = Request(proxy_url=config.REQUEST_KWARGS['proxy_url'], urllib3_proxy_kwargs=config.REQUEST_KWARGS['urllib3_proxy_kwargs'])
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def notify_ending(message, chat_id):
    bot = telegram.Bot(token=config.TOKEN, request=ProxyRequest)
    bot.sendMessage(chat_id=chat_id, text=message)


app = Flask(__name__)

@app.route('/')
def index():
    return 'usage'

@app.route('/send_message')
def send_message():
    chat_id = request.args.get('chat_id', default=0)
    message = request.args.get('message', default = '')
    logger.info(f'chat_id: {chat_id}, message: {message}')
    try:
        notify_ending(message, chat_id)
        answer = {'result': 'SUCCESS'}
    except Exception  as e:
        answer = {'result': 'FAIL', 'error': str(e)}
    return answer

if __name__ == "__main__":
    app.run(debug=True)

