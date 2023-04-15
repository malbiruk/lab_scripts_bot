import requests
import random
import json
import traceback
import telebot

TOKEN = '5961004234:AAGgpbuWwnSc382mXL14m97Glu96_z2nBng'

bot = telebot.TeleBot(TOKEN, parse_mode='MARKDOWN')


def get_citation() -> str:
    '''
    generate random motivational citation using zenquotes.io
    '''
    emoji_list = [
        '✨', '💪', '🙌', '🫶', '🙆‍♀️', '♡', '😌', '🧘', '👍', '👌',
        '🖖', '🤙', '🌈', '😄', '✌', '<3', '🫂', '🤗', '😉', '☘',
        '🤞', '🔥', '🤌']
    citation = requests.get('https://zenquotes.io/api/random').json()[0]
    # return f'‟{citation["q"]}”\n\n_© {citation["a"]}_'
    return f'{citation["q"]} {random.choice(emoji_list)}'


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hello! 🖖
I will support you with motivational citations every time you speak to me 🫂\
""")


@bot.message_handler(func=lambda message: True)
def get_text_messages(message):
    bot.send_message(message.chat.id, get_citation())


def main():
    bot.infinity_polling()


if __name__ == '__main__':
    main()
