import telebot
from telebot.types import InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup
import random
import string
from main_db import readTable, writeTable

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
work_experience = ''
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
    bot.send_message(message.chat.id, '👋Привіт,{}!👋\n'
                                      '😃Це бот для створення резюме, думаю тобі сподобається😃'.format(message.from_user.first_name), reply_markup=but_create())
    print(user_id, message)


@bot.message_handler(content_types=['text'])
def message_reply(message):
    global user_id
    user_id = message.chat.id
    if message.text == '📄Створити резюме📄':
        reply_markup1 = ReplyKeyboardMarkup(resize_keyboard=True)
        msg = bot.send_message(message.chat.id, 'Напишіть ваше ім’я і прізвище', reply_markup=reply_markup1)
        bot.register_next_step_handler(msg, get_name_surname)


def get_name_surname(message):
    global name_surname, update
    if message.text == '-' and not update:
        msg = bot.send_message(message.chat.id, 'Напишіть ваш номер телефону')
        bot.register_next_step_handler(msg, get_phone_number)
    elif message.text == '/start':
        bot.clear_step_handler(message)
        start(message)
        print(name_surname)
    if update:
        name_surname = message.text
        bot.send_message(message.chat.id, 'Хочете ще щось змінити?', reply_markup=end_keyboard())
        update = False
    else:
        msg = bot.send_message(message.chat.id, 'Напишіть ваш номер телефону☎')
        name_surname = message.text
        bot.register_next_step_handler(msg, get_phone_number)
    print('surname =', name_surname)


def get_phone_number(message):
    global phone_number, update
    if message.text == '-' and not update:
        msg = bot.send_message(message.chat.id, 'Напишіть ваш email')
        bot.register_next_step_handler(msg, get_email)
    elif message.text == '/start':
        bot.clear_step_handler(message)
        start(message)
    if update:
        phone_number = message.text
        bot.send_message(message.chat.id, 'Хочете ще щось змінити?', reply_markup=end_keyboard())
        update = False
    else:
        msg = bot.send_message(message.chat.id, 'Напишіть ваш email')
        phone_number = message.text
        bot.register_next_step_handler(msg, get_email)
    print('phone number = ', phone_number)


def get_email(message):
    global email, update
    if message.text == '-' and not update:
        msg = bot.send_message(message.chat.id, 'Напишіть про вашу освіту')
        bot.register_next_step_handler(msg, get_education)
    elif message.text == '/start':
        start(message)
    if update:
        email = message.text
        bot.send_message(message.chat.id, 'Хочете ще щось змінити?', reply_markup=end_keyboard())
        update = False
    else:
        msg = bot.send_message(message.chat.id, 'Напишіть про вашу освіту')
        email = message.text
        bot.register_next_step_handler(msg, get_education)
    print('email = ', email)


def get_education(message):
    global education, update
    if message.text == '-' and not update:
        msg = bot.send_message(message.chat.id, 'Напишіть про ваші навички')
        bot.register_next_step_handler(msg, get_skills)
    elif message.text == '/start':
        start(message)
    if update:
        education = message.text
        bot.send_message(message.chat.id, 'Хочете ще щось змінити?', reply_markup=end_keyboard())
        update = False
    else:
        msg = bot.send_message(message.chat.id, 'Напишіть про ваші навички')
        education = message.text
        bot.register_next_step_handler(msg, get_skills)
    print('education =', education)


def get_skills(message):
    global skills, update
    if message.text == '-' and not update:
        msg = bot.send_message(message.chat.id, 'Вставте посилання на ваші проекти')
        bot.register_next_step_handler(msg, get_projects)
    elif message.text == '/start':
        start(message)
    if update:
        skills = message.text
        bot.send_message(message.chat.id, 'Хочете ще щось змінити?', reply_markup=end_keyboard())
        update = False
    else:
        msg = bot.send_message(message.chat.id, 'Вставте посилання на ваші проекти')
        skills = message.text
        bot.register_next_step_handler(msg, get_projects)
    print('skills = ', skills)


def get_projects(message):
    global projects, update
    if message.text == '-' and not update:
        msg = bot.send_message(message.chat.id, 'Напишіть якими мовами ви володієте')
        bot.register_next_step_handler(msg, get_lang)
    elif message.text == '/start':
        start(message)
    if update:
        projects = message.text
        bot.send_message(message.chat.id, 'Хочете ще щось змінити?', reply_markup=end_keyboard())
        update = False
    else:
        msg = bot.send_message(message.chat.id, 'Напишіть якими мовами ви володієте')
        projects = message.text
        bot.register_next_step_handler(msg, get_lang)
    print('projects = ', projects)


def get_lang(message):
    global lang, update
    if message.text == '-' and not update:
        msg = bot.send_message(message.chat.id, 'Напишіть про рівень знання цих мов')
        bot.register_next_step_handler(msg, get_lang_level)
    elif message.text == '/start':
        start(message)
    if update:
        lang = message.text
        bot.send_message(message.chat.id, 'Хочете ще щось змінити?', reply_markup=end_keyboard())
        update = False
    else:
        msg = bot.send_message(message.chat.id, 'Напишіть про рівень знання цих мов')
        lang = message.text
        bot.register_next_step_handler(msg, get_lang_level)
    print('lang = ', lang)


def get_lang_level(message):
    global lang_level, update
    if message.text == '-' and not update:
        msg = bot.send_message(message.chat.id, 'Напишіть в якій країні ви живете')
        bot.register_next_step_handler(msg, get_country)
    elif message.text == '/start':
        start(message)
    if update:
        lang_level = message.text
        bot.send_message(message.chat.id, 'Хочете ще щось змінити?', reply_markup=end_keyboard())
        update = False
    else:
        msg = bot.send_message(message.chat.id, 'Напишіть в якій країні ви живете')
        lang_level = message.text
        bot.register_next_step_handler(msg, get_country)
    print('lang_level = ', lang_level)


def get_country(message):
    global country, update
    if message.text == '-' and not update:
        msg = bot.send_message(message.chat.id, 'Напишіть в якому місті ви живете')
        bot.register_next_step_handler(msg, get_city)
    elif message.text == '/start':
        start(message)
    if update:
        country = message.text
        bot.send_message(message.chat.id, 'Хочете ще щось змінити?', reply_markup=end_keyboard())
        update = False
    else:
        msg = bot.send_message(message.chat.id, 'Напишіть в якому місті ви живете')
        country = message.text
        bot.register_next_step_handler(msg, get_city)
    print('country =', country)


def get_city(message):
    global city, update
    if message.text == '-' and not update:
        msg = bot.send_message(message.chat.id, 'Напишіть на яку посаду претендуєте')
        bot.register_next_step_handler(msg, get_profession)
    elif message.text == '/start':
        start(message)
    if update:
        city = message.text
        bot.send_message(message.chat.id, 'Хочете ще щось змінити?', reply_markup=end_keyboard())
        update = False
    else:
        msg = bot.send_message(message.chat.id, 'Напишіть на яку посаду претендуєте')
        city = message.text
        bot.register_next_step_handler(msg, get_profession)
    print('city =', city)


def get_profession(message):
    global profession, update
    if message.text == '-' and not update:
        msg = bot.send_message(message.chat.id, 'Напишіть ваші очікування від роботи')
        bot.register_next_step_handler(msg, get_description)
    elif message.text == '/start':
        start(message)
    if update:
        profession = message.text
        bot.send_message(message.chat.id, 'Хочете ще щось змінити?', reply_markup=end_keyboard())
        update = False
    else:
        msg = bot.send_message(message.chat.id, 'Напишіть ваші очікування від роботи')
        profession = message.text
        bot.register_next_step_handler(msg, get_description)
    print('profession =', profession)


def get_description(message):
    global description, update
    if message.text == '-' and not update:
        msg = bot.send_message(message.chat.id, 'Напишіть про ваш минулий досвід роботи')
        bot.register_next_step_handler(msg, get_work_experience)
    elif message.text == '/start':
        start(message)
    if update:
        description = message.text
        bot.send_message(message.chat.id, 'Хочете ще щось змінити?', reply_markup=end_keyboard())
        update = False
    else:
        msg = bot.send_message(message.chat.id, 'Напишіть про ваш минулий досвід роботи')
        description = message.text
        bot.register_next_step_handler(msg, get_work_experience)
    print('description =', description)


def end_keyboard():
    markup = InlineKeyboardMarkup(row_width=1)
    but1 = InlineKeyboardButton('Так', callback_data='15')
    but2 = InlineKeyboardButton('Ні', callback_data='16')
    markup.add(but1, but2)
    return markup


def get_work_experience(message):
    global work_experience, update
    if message.text == '-' and not update:
        bot.send_message(message.chat.id, 'Напишіть про вашу минулу роботу')
    elif message.text == '/start':
        start(message)
    else:
        work_experience = message.text
    bot.send_message(message.chat.id, "😎Ваше резюме готове, перевірте свої дані:😎\n"
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
                                      f"Ваша минулий  досвід роботи: {work_experience}\n"
                                      "Чи хочете відредагувати свої дані?'\n", reply_markup=end_keyboard())
    print('work_experience = ', work_experience)


def changes():
    markup = InlineKeyboardMarkup(row_width=1)
    but1 = InlineKeyboardButton("😃Ім'я та прізвище😃", callback_data='1')
    but2 = InlineKeyboardButton("☎Номер телефону☎️", callback_data='2')
    but3 = InlineKeyboardButton("📧Email📧", callback_data='3')
    but4 = InlineKeyboardButton("🧐Освіта🧐", callback_data='4')
    but5 = InlineKeyboardButton("😄Навички😄", callback_data='5')
    but6 = InlineKeyboardButton("😲Проекти😲", callback_data='6')
    but7 = InlineKeyboardButton("✌Мови✌️", callback_data='7')
    but8 = InlineKeyboardButton("🗣Рівень мови🗣", callback_data='8')
    but9 = InlineKeyboardButton("👍Країна👍", callback_data='9')
    but10 = InlineKeyboardButton("🤟Місто🤟", callback_data='10')
    but11 = InlineKeyboardButton("👨‍🎓Професія👨‍🎓", callback_data='11')
    but12 = InlineKeyboardButton("😱Очікування😱", callback_data='12')
    but13 = InlineKeyboardButton("🤯Досвід роботи🤯", callback_data='13')
    markup.add(but1, but2, but3, but4, but5, but6, but7, but8, but9, but10, but11, but12, but13)
    return markup


@bot.callback_query_handler(func=lambda c: True)
def go_changes(call):
    global update, rand_password
    if call.data == '15':
        bot.send_message(call.from_user.id, 'Що бажаєте змінити?', reply_markup=changes())
    if call.data == '16':
        rand_password = generate_password()
        bot.send_message(call.from_user.id, 'Майже все готово')
        writeTable(user_id, name_surname, phone_number, email, education, skills, projects, lang, lang_level, country, city, work_experience, rand_password, description, profession)
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
        msg = bot.send_message(call.from_user.id, 'Напишіть ваш email')
        bot.register_next_step_handler(msg, get_email)
    if call.data == '4':
        update = True
        msg = bot.send_message(call.from_user.id, 'Напишіть про вашу освіту')
        bot.register_next_step_handler(msg, get_education)
    elif call.data == '5':
        update = True
        msg = bot.send_message(call.from_user.id, 'Напишіть про ваші навички')
        bot.register_next_step_handler(msg, get_skills)
    if call.data == '6':
        update = True
        msg = bot.send_message(call.from_user.id, 'Напишіть про ваші проекти або надішліть посилання на них')
        bot.register_next_step_handler(msg, get_projects)
    elif call.data == '7':
        update = True
        msg = bot.send_message(call.from_user.id, 'Напишіть якими мовами ви володієте')
        bot.register_next_step_handler(msg, get_lang)
    if call.data == '8':
        update = True
        msg = bot.send_message(call.from_user.id, 'Напишіть рівень знання цих мов')
        bot.register_next_step_handler(msg, get_lang_level)
    elif call.data == '9':
        update = True
        msg = bot.send_message(call.from_user.id, 'Напишіть в якій країні ви живете')
        bot.register_next_step_handler(msg, get_country)
    if call.data == '10':
        update = True
        msg = bot.send_message(call.from_user.id, 'Напишіть в якому місті ви живете')
        bot.register_next_step_handler(msg, get_city)
    elif call.data == '11':
        update = True
        msg = bot.send_message(call.from_user.id, 'Напишіть на яку посаду претендуєте')
        bot.register_next_step_handler(msg, get_profession)
    if call.data == '12':
        update = True
        msg = bot.send_message(call.from_user.id, 'Напишіть ваші очікування від роботи')
        bot.register_next_step_handler(msg, get_description)
    elif call.data == '13':
        update = True
        msg = bot.send_message(call.from_user.id, 'Напишіть про ваш минулий досвід роботи')
        bot.register_next_step_handler(msg, get_work_experience)
    if call.data == '16':
        update = True
        telegram_id = call.from_user.id
        bot.send_message(call.from_user.id, f"🥳Ваше резюме готове🥳\n"
                                            f"🥸Ось ваші дані для реєстрації на сайті:🥸\n"
                                            f"🤐Telegram ID: {telegram_id}🤐\n"
                                            f"🤐Ваш пароль: {rand_password}🤐")


bot.polling(none_stop=True)
