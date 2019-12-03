#!/usr/bin/env python3

import json
import telegram
import config
from telegram.utils.request import Request
ProxyRequest = Request(proxy_url=config.REQUEST_KWARGS['proxy_url'], urllib3_proxy_kwargs=config.REQUEST_KWARGS['urllib3_proxy_kwargs'])
chat = ''

def notify_ending(message, chat):
    bot = telegram.Bot(token=config.TOKEN, request=ProxyRequest)
    bot.sendMessage(chat_id=chat, text=message)


if __name__ == "__main__":
    message = "AZAZA"
    notify_ending(message, chat)

