from app import app
from flask import render_template, Flask
from flask import render_template, flash, redirect, url_for, request

from app.main_db import readTable

from app.forms import LoginForm




@app.route("/")
@app.route("/index/")
def index():
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

    def portal():
        nonlocal name_surname, phone_number, email, education, skills, projects, lang, lang_level, \
                            country, city, past_work, description, profession, user_id
        result = readTable()
        profession = result[0][-1]
        name_surname = result[0][1]
        phone_number = result[0][2]
        email = result[0][3]
        education = result[0][4]
        skills = result[0][5]
        projects = result[0][6]
        lang = result[0][7]
        lang_level = [0]
        country = result[0][9]
        city = result[0][10]
        past_work = result[0][11]
        description = result[0][-2]


    portal()
    return render_template('index.html', profession=profession, name_surname=name_surname, phone_number=phone_number,\
                           email=email, education=education, skills=skills, projects=projects, lang=lang,\
                           lang_level=lang_level, country=country, city=city, past_work=past_work, description=description)


@app.route('/login', methods=['GET', 'POST'])
def login():
    result = readTable()
    user_id = result[0][0]
    rand_password = result[0][-4]
    form = LoginForm()
    if form.validate_on_submit and request.method == 'POST':
        password = form.password.data
        if password == rand_password:
            return redirect(url_for('index.html'))
        else:
            return render_template('login.html', title='Sign In', form=form)

    return render_template('login.html', form=form, rand_password=rand_password, user_id=user_id)