import os
import telebot
import json

TOKEN = os.getenv('TG_BRAIN_WAKER_TOKEN')
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.reply_to(message, "Hi! You are my slave now.")
    data = []
    read_file = open('subscribers.json', 'r')
    data = json.load(read_file)
    if not message.chat.id in data['subscribers']:
        data['subscribers'].append(message.chat.id)
    read_file.close()
    write_file = open('subscribers.json', 'w')
    json.dump(data, write_file, indent=4)
    write_file.close()

def init_subscribers_data():
    with open('subscribers.json', 'w') as file:
        json.dump({'subscribers' : []}, file, indent=4)

def main():
    init_subscribers_data()
    bot.infinity_polling()

if __name__ == '__main__':
    main()
