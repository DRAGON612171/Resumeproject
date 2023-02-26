import time
import telebot
from telebot.types import InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup
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
update = False


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
    if message.text == '-' and not update:
        msg = bot.send_message(message.chat.id, 'Напишіть ваш номер телефону')
        bot.register_next_step_handler(msg, get_phone_number)
    elif message.text == '/start' and not update:
        bot.clear_step_handler(message)
        start(message)
        print(name_surname)
    if update:
        name_surname = message.text
        bot.send_message(message.chat.id, 'Хочете ще щось змінити?', reply_markup=end())
    else:
        msg = bot.send_message(message.chat.id, 'Напишіть ваш номер телефону')
        name_surname = message.text
        bot.register_next_step_handler(msg, get_phone_number)
    print('surname =', name_surname)


def get_phone_number(message):
    global phone_number
    if message.text == '-' and not update:
        msg = bot.send_message(message.chat.id, 'Напишіть ваш email')
        bot.register_next_step_handler(msg, get_email)
    elif message.text == '/start' and not update:
        bot.clear_step_handler(message)
        start(message)
    if update:
        phone_number = message.text
        bot.send_message(message.chat.id, 'Хочете ще щось змінити?', reply_markup=end())
    else:
        msg = bot.send_message(message.chat.id, 'Напишіть ваш email')
        phone_number = message.text
        bot.register_next_step_handler(msg, get_email)
    print('phone number = ', phone_number)


def get_email(message):
    global email
    if message.text == '-' and not update:
        msg = bot.send_message(message.chat.id, 'Напишіть про вашу освіту')
        bot.register_next_step_handler(msg, get_education)
    elif message.text == '/start' and not update:
        start(message)
    if update:
        email = message.text
        bot.send_message(message.chat.id, 'Хочете ще щось змінити?', reply_markup=end())
    else:
        msg = bot.send_message(message.chat.id, 'Напишіть про вашу освіту')
        email = message.text
        bot.register_next_step_handler(msg, get_education)
    print('email = ', email)


def get_education(message):
    global education
    if message.text == '-' and not update:
        msg = bot.send_message(message.chat.id, 'Напишіть про ваші навички')
        bot.register_next_step_handler(msg, get_skills)
    elif message.text == '/start' and not update:
        start(message)
    if update:
        education = message.text
        bot.send_message(message.chat.id, 'Хочете ще щось змінити?', reply_markup=end())
    else:
        msg = bot.send_message(message.chat.id, 'Напишіть про ваші навички')
        education = message.text
        bot.register_next_step_handler(msg, get_skills)
    print('education =', education)


def get_skills(message):
    global skills
    if message.text == '-' and not update:
        msg = bot.send_message(message.chat.id, 'Вставте посилання на ваші проекти')
        bot.register_next_step_handler(msg, get_projects)
    elif message.text == '/start' and not update:
        start(message)
    if update:
        skills = message.text
        bot.send_message(message.chat.id, 'Хочете ще щось змінити?', reply_markup=end())
    else:
        msg = bot.send_message(message.chat.id, 'Вставте посилання на ваші проекти')
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


def end():
    markup = InlineKeyboardMarkup(row_width=1)
    but1 = InlineKeyboardButton('Так', callback_data='15')
    but2 = InlineKeyboardButton('Ні', callback_data='16')
    markup.add(but1, but2)
    return markup


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
                                      f"Ваша минула робота: {past_work}\n"
                                      "Чи хочете відредагувати свої дані?'\n", reply_markup=end())
    #writeTable(user_id, name_surname, phone_number, email, education, skills, projects, lang, lang_level, country, city, past_work, rand_password, description, profession)
    print('work_experience = ', past_work)


def changes():
    markup = InlineKeyboardMarkup(row_width=1)
    but1 = InlineKeyboardButton("Ім'я та прізвище", callback_data='1')
    but2 = InlineKeyboardButton("Номер телефону", callback_data='2')
    but3 = InlineKeyboardButton("Email", callback_data='3')
    but4 = InlineKeyboardButton("Освіта", callback_data='4') #Roma
    but5 = InlineKeyboardButton("Навички", callback_data='5') #Roma
    but6 = InlineKeyboardButton("Проекти", callback_data='6') #Dima
    but7 = InlineKeyboardButton("Мови", callback_data='7')  #Dima
    but8 = InlineKeyboardButton("Рівень мови", callback_data='8') #Dima
    but9 = InlineKeyboardButton("Країна", callback_data='9') #Dima
    but10 = InlineKeyboardButton("Місто", callback_data='10') #Nazar
    but11 = InlineKeyboardButton("Професія", callback_data='11')  #Nazar
    but12 = InlineKeyboardButton("Очікування", callback_data='12') #Nazar
    but13 = InlineKeyboardButton("Досвід роботи", callback_data='13') #Nazar
    markup.add(but1, but2, but3, but4, but5, but6, but7, but8, but9, but10, but11, but12, but13)
    return markup


@bot.callback_query_handler(func=lambda c: True)
def go_changes(call, id, name_surname, phone_number, email, education, skills, projects, lang, lang_level, country, city, past_work, description, profession):
    global update, rand_password
    if call.data == '15':
        bot.send_message(call.from_user.id, 'Що бажаєте змінити?', reply_markup=changes())
    if call.data == '16':
        rand_password = generate_password()
        bot.send_message(call.from_user.id, 'Майже все готово')
        writeTable(id, name_surname, phone_number, email, education, skills, projects, lang, lang_level, country, city, past_work, rand_password, description, profession)
    elif call.data == '1':
        update = True
        msg = bot.send_message(call.from_user.id, 'Напишіть ваше ім’я і прізвище')
        bot.register_next_step_handler(msg, get_name_surname)
    if call.data == '2':
        update = True
        msg = bot.send_message(call.from_user.id, 'Напишіть ваш номер телефону')
        bot.register_next_step_handler(msg, get_phone_number)
    elif call.data == '3':
        update = True
        msg = bot.send_message(call.from_user.id, 'Напишіть про вашу освіту')
        bot.register_next_step_handler(msg, get_email)
    if call.data == '4':
        update = True
        msg = bot.send_message(call.from_user.id, 'Напишіть про ваші навички')
        bot.register_next_step_handler(msg, get_education)
    elif call.data == '5':
        update = True
        msg = bot.send_message(call.from_user.id, 'Вставте посилання на ваші проекти')
        bot.register_next_step_handler(msg, get_skills)


bot.polling(none_stop=True)
