import time
import telebot
from telebot.types import InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import random
import string

bot = telebot.TeleBot("5662928795:AAHhdf4WxBx_CGY1x5CU85Y5qR06Y3UgcFQ")

name = ''
surname = ''
phone_number = ''
email = ''
education = ''
skills = ''
lang = ''
lang_level = ''
location = ''
work_experience = ''
user_id = ''
rand_password = ""
# можна додати ще пункт з своєю мотивацією
#У кінці треба вивести всі данні, щоб користувач все перевірив


def but_create():
    reply_markup = ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = KeyboardButton('📄Створити резюме📄')
    reply_markup.add(but1)
    return reply_markup


def generate_password():
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(8))


@bot.message_handler(commands=['start'])                            #можна додати команду, щоб редагувати вже записані відповіді(або кейборд кнопкою)
def start(message):
    user_id = message.chat.id
    bot.send_message(message.chat.id, 'Привіт,{}!\n '
                                      'Це бот для створення резюме, думаю тобі сподобається'.format(message.from_user.first_name), reply_markup=but_create())
    print(user_id, message)


@bot.message_handler(content_types=['text'])
def message_reply(message):
    global name
    start(message)
    if message.text == '📄Створити резюме📄':
        reply_markup1 = ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(message.chat.id, 'Напишіть ваше ім’я', reply_markup=reply_markup1)
        bot.register_next_step_handler(msg, get_user_name)



def get_user_name(message):
    start(message)
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
    msg = bot.send_message(message.chat.id, 'Напишіть про вашу освіту')   #замість другого напішіть, що ви хочете питати наступне
    bot.register_next_step_handler(msg, get_education)                  #замість другого напишіть наступну функцію
    print('email = ', email)


def get_education(message):
    global education
    if message.text:
        education = message.text
    elif message.text == '-':
        pass
    msg = bot.send_message(message.chat.id, 'Напишіть про ваші навички')
    bot.register_next_step_handler(msg, get_skills)
    print('education ', education)


def get_skills(message):
    global skills
    if message.text:
        skills = message.text
    elif message.text == '-':
        pass
    msg = bot.send_message(message.chat.id, 'Напишіть якими мовами ви володієте')
    bot.register_next_step_handler(msg, get_lang)
    print('skills = ', skills)


def get_lang(message):
    global lang
    if message.text:
        lang = message.text
    elif message.text == '-':
        pass
    msg = bot.send_message(message.chat.id, 'Напишіть про рівень знання цих мов')         #замість другого напиши, що ти хочеш питати наступне(lang_level)
    bot.register_next_step_handler(msg, get_lang_level)                                #замість другого напиши наступну функцію
    print('lang = ', lang)


def get_lang_level(message):
    global lang_level
    if message.text:
        lang_level = message.text
    elif message.text == '-':
        pass
    msg = bot.send_message(message.chat.id, 'Напишіть де ви живете ')
    bot.register_next_step_handler(msg, get_location)
    print('lang_level = ', lang_level)


def get_location(message):
    global location
    if message.text:
        location = message.text
    elif message.text == '-':
        pass
    msg = bot.send_message(message.chat.id, 'Напишіть про ваш досвід роботи')
    bot.register_next_step_handler(msg, get_work_experience)
    print('location =', location)


def get_work_experience(message):
    global work_experience
    if message.text:
        work_experience = message.text
    elif message.text == '-':
        pass
    bot.send_message(message.chat.id, 'Ваше резюме готове')
    print('work_experience = ', work_experience)
    rand_password = generate_password()
    print(rand_password)






bot.polling(none_stop=True)
