import time
import telebot
from telebot.types import InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

bot = telebot.TeleBot("5662928795:AAHhdf4WxBx_CGY1x5CU85Y5qR06Y3UgcFQ")

name = ''
surname = ''
phone_number = ''
email = ''
education = ''
skills = ''
lang = ''
lang_level = ''
recommendations = ''
location = ''
work_experience = ''


@bot.message_handler(commands=['start'])                            #можна додати команду, щоб редагувати вже записані відповіді(або кейборд кнопкою)
def button_message(message):
    reply_markup = ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = KeyboardButton('📄Створити резюме📄')
    reply_markup.add(but1)
    bot.send_message(message.chat.id, 'Привіт,{}!\n '
                                      'Це бот для створення резюме, думаю тобі сподобається'.format(message.from_user.first_name), reply_markup=reply_markup)


@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text == '📄Створити резюме📄':
        reply_markup1 = ReplyKeyboardMarkup(resize_keyboard=True)               # Пропоную кнопки написати у окремиих функціях
        but2 = KeyboardButton("Запам'ятати відповідь")                          # Треба записувати дані користувача в зміні
        reply_markup1.add(but2)
        bot.send_message(message.chat.id, 'Напишіть ваше ім’я', reply_markup=reply_markup1)
    elif message.text == "Запам'ятати відповідь":                               # Після відхилення код буде йти по колу
        reply_markup2 = ReplyKeyboardMarkup(resize_keyboard=True)
        but3 = KeyboardButton("Так")
        but4 = KeyboardButton("Ні")
        reply_markup2.add(but3, but4)
        bot.send_message(message.chat.id, 'Чи хочете ви відредагувати відповідь на запитання?', reply_markup=reply_markup2)
    elif message.text == "Ні":
        reply_markup1 = ReplyKeyboardMarkup(resize_keyboard=True)
        but2 = KeyboardButton("Запам'ятати відповідь")
        reply_markup1.add(but2)
        bot.send_message(message.chat.id, 'Напишіть ваше прізвище', reply_markup=reply_markup1)


bot.polling(none_stop=True)
