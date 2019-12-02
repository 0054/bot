#!/usr/bin/env python3

import json
import telegram
import config

def notify_ending(message):
    bot = telegram.Bot(token=config.token)
    bot.sendMessage(chat_id=config.alert_chat, text=message)


if __name__ == "__main__":
    message = "AZAZA"
    notify_ending(message)

