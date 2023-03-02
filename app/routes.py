from app import app
from flask import render_template

from main_db import readTable


@app.route("/")
@app.route("/index/")
def index():
    profession = ''
    name_surname = ''
    phone_number = ''
    email = ''
    education = ''
    skills, projects, lang, lang_level = list()
    country = ''
    city = ''
    past_work = ''
    user_id = ''
    rand_password = ''
    description = ''

    def portal():
        nonlocal name_surname, phone_number, email, education, skills, projects, lang, lang_level, \
                            country, city, past_work, description, profession
        result = readTable()
        profession = result[-1]
        name_surname = result[1]
        phone_number = result[2]
        email = result[3]
        education = result[4]
        skills = result[5]
        projects = result[6]
        lang = result[7]
        lang_level = list()
        country = result[9]
        city = result[10]
        past_work = result[11]
        description = result[-2]

    portal()
    return render_template('index.html', profession=profession, name_surname=name_surname, phone_number=phone_number,\
                           email=email, education=education, skills=skills, projects=projects, lang=lang,\
                           lang_level=lang_level, country=country, city=city, past_work=past_work, description=description)
