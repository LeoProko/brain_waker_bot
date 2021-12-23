import time
import json
import os
import random

from telebot import TeleBot

TOKEN = os.getenv("TG_BRAIN_WAKER_TOKEN")
bot = TeleBot(TOKEN)


def get_random_hex() -> str:
    return str(hex(random.randint(20, 50)))


def send_tasks() -> None:
    with open("subscribers.json", "r", encoding="utf8") as file:
        try:
            data = json.load(file)
        except BaseException:
            return
        if "subscribers" not in data or len(data["subscribers"]) == 0:
            return
        for chat_id in data["subscribers"]:
            bot.send_message(chat_id, "Convert")
            bot.send_message(chat_id, get_random_hex() + " + " + get_random_hex())
            bot.send_message(chat_id, "from hexadecimal to decimal")


def sender() -> None:
    while True:
        send_tasks()
        time.sleep(random.randint(60 * 60 * 1, 60 * 60 * 3))
