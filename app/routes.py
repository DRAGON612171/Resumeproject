from app import app
from flask import render_template

from app.main_db import readTable


@app.route("/")
@app.route("/index/")
def index():
    profession = ''
    name_surname = ''
    phone_number = ''
    email = ''
    education = ''
    tech_skills, soft_skills, projects, lang, lang_level = list(), list(), list(), '', ''
    country = ''
    city = ''
    past_work = ''
    user_id = ''
    rand_password = ''
    description = ''

    def portal():
        nonlocal name_surname, phone_number, email, education, tech_skills, projects, lang, lang_level, \
                            country, city, past_work, description, profession
        result = readTable()
        profession = result[0][-1]
        name_surname = result[0][1]
        phone_number = result[0][2]
        email = result[0][3]
        education = result[0][4]
        tech_skills = result[0][5]
        projects = result[0][6]
        lang = result[0][7]
        lang_level = result[0][8]
        country = result[0][9]
        city = result[0][10]
        past_work = result[0][11]
        description = result[0][-2]

    portal()
    return render_template('index.html', profession=profession, name_surname=name_surname, phone_number=phone_number,\
                           email=email, education=education, tech_skills=tech_skills, projects=projects, lang=lang,\
                           lang_level=lang_level, country=country, city=city, past_work=past_work, description=description)

