import time
import telebot
from telebot.types import InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

bot = telebot.TeleBot("5662928795:AAHhdf4WxBx_CGY1x5CU85Y5qR06Y3UgcFQ")

name = ''
surname = ''
phone_number = ''
email = ''
education = ''              #Діма
skills = ''                 #Діма
lang = ''                   #Діма
lang_level = ''             #Назар
location = ''               #Назар
work_experience = ''        #Назар
# можна додати ще пункт з своєю мотивацією
#У кінці треба вивести всі данні, щоб користувач все перевірив

def but_create():
    reply_markup = ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = KeyboardButton('📄Створити резюме📄')
    reply_markup.add(but1)
    return reply_markup


@bot.message_handler(commands=['start'])                            #можна додати команду, щоб редагувати вже записані відповіді(або кейборд кнопкою)
def button_message(message):
    bot.send_message(message.chat.id, 'Привіт,{}!\n '
                                      'Це бот для створення резюме, думаю тобі сподобається'.format(message.from_user.first_name), reply_markup=but_create())
    print(message)


@bot.message_handler(content_types=['text'])
def message_reply(message):
    global name
    if message.text == '📄Створити резюме📄':
        reply_markup1 = ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(message.chat.id, 'Напишіть ваше ім’я', reply_markup=reply_markup1)
        bot.register_next_step_handler(msg, get_user_name)


def get_user_name(message):
    global name
    if message.text:
        name = message.text
    elif message.text == '-':
        pass
    msg = bot.send_message(message.chat.id, 'Напишіть ваше прізвище')
    bot.register_next_step_handler(msg, get_surname)
    print('name = ', name)


def get_surname(message):
    global surname
    if message.text:
        surname = message.text
    elif message.text == '-':
        pass
    msg = bot.send_message(message.chat.id, 'Напишіть ваш номер телефону')
    bot.register_next_step_handler(msg, get_phone_number)
    print('surname=', surname)


def get_phone_number(message):
    global phone_number
    if message.text:
        phone_number = message.text
    elif message.text == '-':
        pass
    msg = bot.send_message(message.chat.id, 'Напишіть ваш email')
    bot.register_next_step_handler(msg, get_email)
    print('phone number = ', phone_number)


def get_email(message):
    global email
    if message.text:
        email = message.text
    elif message.text == '-':
        pass
    # msg = bot.send_message(message.chat.id, 'Напишіть ваш email')   #замість другого напішіть, що ви хочете питати наступне
    # bot.register_next_step_handler(msg, get_email)                  #замість другого напишіть наступну функцію
    print('email = ', email)


bot.polling(none_stop=True)
