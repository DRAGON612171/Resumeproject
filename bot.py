import time
import telebot
from telebot.types import InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import random
import string
from db import readTable, writeTable

bot = telebot.TeleBot("5662928795:AAHhdf4WxBx_CGY1x5CU85Y5qR06Y3UgcFQ")

profession = ''
name_surname = ''
phone_number = ''
email = ''
education = ''
skills = list()
projects = list()
lang = list()
lang_level = list()
country = ''
city = ''
past_work = ''
user_id = ''
rand_password = ''
description = ''

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
    global user_id
    user_id = message.chat.id
    bot.send_message(message.chat.id, 'Привіт,{}!\n '
                                      'Це бот для створення резюме, думаю тобі сподобається'.format(message.from_user.first_name), reply_markup=but_create())
    print(user_id, message)


@bot.message_handler(content_types=['text'])
def message_reply(message):
    global name_surname
    global user_id
    user_id = message.chat.id
    if message.text == '📄Створити резюме📄':
        reply_markup1 = ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(message.chat.id, 'Напишіть ваше ім’я і прізвище', reply_markup=reply_markup1)
        bot.register_next_step_handler(msg, get_name_surname)


def get_name_surname(message):
    global name_surname
    msg = bot.send_message(message.chat.id, 'Напишіть ваш номер телефону')
    if message.text == '-':
        bot.register_next_step_handler(msg, get_phone_number)
    elif message.text == '/start':
        bot.clear_step_handler(message)
        start(message)
    else:
        name_surname = message.text
        bot.register_next_step_handler(msg, get_phone_number)
    print('surname =', name_surname)


def get_phone_number(message):
    global phone_number
    msg = bot.send_message(message.chat.id, 'Напишіть ваш email')
    if message.text == '-':
        bot.register_next_step_handler(msg, get_email)
    elif message.text == '/start':
        bot.clear_step_handler(message)
        start(message)
    else:
        phone_number = message.text
        bot.register_next_step_handler(msg, get_email)
    print('phone number = ', phone_number)


def get_email(message):
    global email
    msg = bot.send_message(message.chat.id, 'Напишіть про вашу освіту')
    if message.text == '-':
        bot.register_next_step_handler(msg, get_education)
    elif message.text == '/start':
        start(message)
    else:
        email = message.text
        bot.register_next_step_handler(msg, get_education)
    print('email = ', email)


def get_education(message):
    global education
    msg = bot.send_message(message.chat.id, 'Напишіть про ваші навички')
    if message.text == '-':
        bot.register_next_step_handler(msg, get_skills)
    elif message.text == '/start':
        start(message)
    else:
        education = message.text
        bot.register_next_step_handler(msg, get_skills)
    print('education =', education)


def get_skills(message):
    global skills
    msg = bot.send_message(message.chat.id, 'Вставте посилання на ваші проекти')
    if message.text == '-':
        bot.register_next_step_handler(msg, get_projects)
    elif message.text == '/start':
        start(message)
    else:
        skills = message.text
        bot.register_next_step_handler(msg, get_projects)
    print('skills = ', skills)


def get_projects(message):
    global projects
    msg = bot.send_message(message.chat.id, 'Напишіть якими мовами ви володієте')
    if message.text == '-':
        bot.register_next_step_handler(msg, get_lang)
    elif message.text == '/start':
        start(message)
    else:
        projects = message.text
        bot.register_next_step_handler(msg, get_lang)
    print('projects = ', projects)


def get_lang(message):
    global lang
    msg = bot.send_message(message.chat.id, 'Напишіть про рівень знання цих мов')
    if message.text == '-':
        bot.register_next_step_handler(msg, get_lang_level)
    elif message.text == '/start':
        start(message)
    else:
        lang = message.text
        bot.register_next_step_handler(msg, get_lang_level)
    print('lang = ', lang)


def get_lang_level(message):
    global lang_level
    msg = bot.send_message(message.chat.id, 'Напишіть з якої ви країни')
    if message.text == '-':
        bot.register_next_step_handler(msg, get_country)
    elif message.text == '/start':
        start(message)
    else:
        lang_level = message.text
        bot.register_next_step_handler(msg, get_country)
    print('lang_level = ', lang_level)


def get_country(message):
    global country
    msg = bot.send_message(message.chat.id, 'Напишіть з якого ви міста')
    if message.text == '-':
        bot.register_next_step_handler(msg, get_city)
    elif message.text == '/start':
        start(message)
    else:
        country = message.text
        bot.register_next_step_handler(msg, get_city)
    print('country =', country)


def get_city(message):
    global city
    msg = bot.send_message(message.chat.id, 'Напишіть на яку посаду претендуєте')
    if message.text == '-':
        bot.register_next_step_handler(msg, get_work_experience)
    elif message.text == '/start':
        start(message)
    else:
        city = message.text
        bot.register_next_step_handler(msg, get_profession)
    print('city =', city)


def get_profession(message):
    global profession
    msg = bot.send_message(message.chat.id, 'Напишіть ваші очікування від роботи')
    if message.text == '-':
        bot.register_next_step_handler(msg, get_description)
    elif message.text == '/start':
        start(message)
    else:
        profession = message.text
        bot.register_next_step_handler(msg, get_description)
    print('profession =', profession)


def get_description(message):
    global description
    msg = bot.send_message(message.chat.id, 'Напишіть про ваш минулий досвід роботи')
    if message.text == '-':
        bot.register_next_step_handler(msg, get_work_experience)
    elif message.text == '/start':
        start(message)
    else:
        description = message.text
        bot.register_next_step_handler(msg, get_work_experience)
    print('description =', description)


def get_work_experience(message):
    global past_work
    if message.text == '-':
        bot.send_message(message.chat.id, 'Ваше резюме готове')
    elif message.text == '/start':
        start(message)
    else:
        past_work = message.text
    bot.send_message(message.chat.id, "Ваше резюме готове, перевірте свої дані:\n"
                                      f"Ім'я та прізивще: {name_surname}\n"  
                                      f"Номер телефону: {phone_number}\n" 
                                      f"Електронна пошта: {email}\n" 
                                      f"Освіта: {education}\n" 
                                      f"Навички: {skills}\n" 
                                      f"Посилання на ваші проекти: {projects}\n"
                                      f"Мови: {lang}\n"
                                      f"Рівень знання цих мов: {lang_level}\n"
                                      f"Ваша країна: {country}\n" 
                                      f"Ваше місто: {city}\n" 
                                      f"Посада на яку претендуєте: {profession}\n" 
                                      f"Ваші очікування від роботи: {description}\n" 
                                      f"Ваша минула робота: {past_work}\n")
    rand_password = generate_password()
    writeTable(user_id, name_surname, phone_number, email, education, skills, projects, lang, lang_level, country, city, past_work, rand_password, description, profession)
    print('work_experience = ', past_work)
    print('password = ', rand_password)


bot.polling(none_stop=True)
