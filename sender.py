import telebot
import time
import json
import os
import random

TOKEN = os.getenv('TG_BRAIN_WAKER_TOKEN')
bot = telebot.TeleBot(TOKEN)

def get_random_hex() -> str:
    return str(hex(random.randint(20, 50)))

while True:
    with open('subscribers.json', 'r', encoding='utf8') as data:
        for chat_id in json.load(data)['subscribers']:
            bot.send_message(chat_id, 'Convert')
            bot.send_message(chat_id, get_random_hex() + ' + ' + get_random_hex())
            bot.send_message(chat_id, 'from hexadecimal to decimal')
    time.sleep(random.randint(60 * 60 * 1, 60 * 60 * 3))