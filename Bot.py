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
    bot.send_message(message.chat.id, 'Ваше резюме готове, якщо хочете перевірити відповіді натисніть кнопку')
    print('work_experience = ', work_experience)