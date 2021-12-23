import os
import json
import asyncio
from telebot.async_telebot import AsyncTeleBot

from sender import send_tasks

TOKEN = os.getenv("TG_BRAIN_WAKER_TOKEN")
async_bot = AsyncTeleBot(TOKEN, parse_mode=None)

@async_bot.message_handler(commands=["start"])
async def start_command(message):
    async_bot.reply_to(message, "Hi! I am a Brain Waker bot.")
    await async_bot.reply_to(
        message,
        (
            "I'm going to send you random task "
            "every one to three hours "
            "to test your brain for fatigue."
        ),
    )
    data = []
    with open("subscribers.json", "r") as file:
        data = json.load(file)
        if message.chat.id not in data["subscribers"]:
            data["subscribers"].append(message.chat.id)
    with open("subscribers.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
    send_tasks()


@async_bot.message_handler(commands=["stop"])
async def stop_command(message):
    await async_bot.reply_to(message, "Bye, bye!")
    data = []
    with open("subscribers.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        if message.chat.id in data["subscribers"]:
            data["subscribers"].remove(message.chat.id)
    with open("subscribers.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def handler():
    asyncio.run(async_bot.polling())
