import os
from dotenv import load_dotenv
import telebot
from telebot import types

load_dotenv()
bot = telebot.TeleBot(os.getenv('BOT_TOKEN'))

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Hello")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 Hello':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Button1')
        btn2 = types.KeyboardButton('Button2')
        btn3 = types.KeyboardButton('Button3')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вас вопрос', reply_markup=markup) #ответ бота


    elif message.text == 'Button1':
        bot.send_message(message.from_user.id, 'Answer1' + '[ссылке](https://mysite.org)', parse_mode='Markdown')

    elif message.text == 'Button2':
        bot.send_message(message.from_user.id, 'Answer2' + '[ссылке](https://mysite.org)', parse_mode='Markdown')

    elif message.text == 'Button3':
        bot.send_message(message.from_user.id, 'Answer3' + '[ссылке](https://mysite.org)', parse_mode='Markdown')


bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть