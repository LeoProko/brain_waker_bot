import os
from telebot.async_telebot import AsyncTeleBot
import json
import asyncio

TOKEN = os.getenv('TG_BRAIN_WAKER_TOKEN')
async_bot = AsyncTeleBot(TOKEN, parse_mode=None)

@async_bot.message_handler(commands=['start'])
async def start_command(message):
    await async_bot.reply_to(message, "Hi! I am a Brain Waker bot.")
    await async_bot.reply_to(message, (
        "I'm going to send you random task "
        "every one to three hours "
        "to test your brain for fatigue."
    ))
    data = []
    with open('subscribers.json', 'r') as file:
        data = json.load(file)
        if not message.chat.id in data['subscribers']:
            data['subscribers'].append(message.chat.id)
    with open('subscribers.json', 'w') as file:
        json.dump(data, file, indent=4)

@async_bot.message_handler(commands=['stop'])
async def start_command(message):
    await async_bot.reply_to(message, "Bye, bye!")
    data = []
    with open('subscribers.json', 'r') as file:
        data = json.load(file)
        if message.chat.id in data['subscribers']:
            data['subscribers'].remove(message.chat.id)
    with open('subscribers.json', 'w') as file:
        json.dump(data, file, indent=4)

def handler():
    asyncio.run(async_bot.polling())