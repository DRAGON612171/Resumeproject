from app import app
from flask import render_template, redirect, url_for
from .forms import LoginForm
from .main_db import readTable

right_tuple = ''


@app.route("/", methods=['GET', 'POST'])
@app.route("/index/", methods=['GET', 'POST'])
def login():
    global right_tuple
    user = LoginForm()
    result = readTable()
    if user.validate_on_submit():
        for data_tuple in result:
            if int(user.user_id.data) in data_tuple and data_tuple[9] == str(user.password.data):
                right_tuple = data_tuple
                return redirect(url_for('resume'))
    return render_template('login_form.html', user=user)


@app.route("/resume", methods=['GET', 'POST'])
def resume():
    profession = ''
    name_surname = ''
    phone_number = ''
    email = ''
    education = ''
    tech_skills, soft_skills, projects, lang, lang_level = list(), list(), list(), '', ''
    country = ''
    city = ''
    past_work = ''
    how_long = ''
    job_description = ''
    user_id = ''
    rand_password = ''
    description = ''

    def portal():
        nonlocal name_surname, phone_number, email, education, tech_skills, soft_skills, projects, lang, lang_level, \
                            country, city, past_work, description, profession, how_long, job_description
        name_surname = right_tuple[1]
        phone_number = right_tuple[2]
        email = right_tuple[3]
        education = right_tuple[4]
        lang = right_tuple[5]
        lang_level = right_tuple[6]
        country = right_tuple[7]
        city = right_tuple[8]
        description = right_tuple[10]
        profession = right_tuple[11]
        past_work = right_tuple[-1]
        job_description = right_tuple[-2]
        how_long = right_tuple[-3]
        projects = right_tuple[-4]
        tech_skills = right_tuple[-5]
        soft_skills = right_tuple[-6]

    portal()

    return render_template('index.html', profession=profession, name_surname=name_surname, phone_number=phone_number,
                           email=email, education=education, tech_skills=tech_skills, soft_skills=soft_skills,
                           projects=projects, lang=lang, lang_level=lang_level, country=country, city=city,
                           past_work=past_work, how_long=how_long, job_description=job_description, description=description)



