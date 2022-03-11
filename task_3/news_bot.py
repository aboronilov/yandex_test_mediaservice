import os

import telebot
from dotenv import load_dotenv
from task_3.news_parser import get_last_news

load_dotenv()
TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['text'])
def send_new(message):

    if message.text.lower() == "привет":
        text = get_last_news()
        bot.send_message(message.from_user.id, text)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Для получения последней новости с vc.ru напишите слово 'привет'")
    else:
        bot.send_message(message.from_user.id, "Для получения справки напишите /help.")


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
