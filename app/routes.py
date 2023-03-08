from app import app
from flask import render_template
from .forms import LoginForm
from app.main_db import readTable

right_tuple = (198483175, 'Валерія Мацібура', '45672384023', 'lavireall@gmail.com', 'КНУ імені Тараса Шевченка', ['English', 'Franch', 'Ukrainian', 'German'], ['B2', 'A2', 'C2', 'A2'], 'UKRAINE',
               'KYIV', 'Nema\n', '123123123', 'хочу працювати в компанії, яка займається нейронними мережами', 'Python Developer', ['friendlyness', 'teamwork', 'else'], ['Postgres', 'Python', 'Git',
 'HTML'], ['link_on_project1', 'link_on_project2'], ['2009 - 2013'], ["В мої обов'язки входило під'єднувати бази даних до Python"])


@app.route("/")
@app.route("/index/")
def login():
    global right_tuple
    user = LoginForm()
    result = readTable()
    for data_tuple in result:
        if user.user_id in data_tuple:
            right_tuple = data_tuple
    return render_template('login_form.html', user=user)



@app.route("/Resume/")
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
    how_long = ''
    job_description = ''
    user_id = ''
    rand_password = ''
    description = ''

    def portal():
        nonlocal name_surname, phone_number, email, education, tech_skills, soft_skills, projects, lang, lang_level, \
                            country, city, past_work, description, profession, how_long, job_description
        profession = right_tuple[12]
        name_surname = right_tuple[1]
        phone_number = right_tuple[2]
        email = right_tuple[3]
        education = right_tuple[4]
        tech_skills = right_tuple[-4]
        soft_skills = right_tuple[-5]
        projects = right_tuple[-3]
        lang = right_tuple[5]
        lang_level = right_tuple[6]
        country = right_tuple[7]
        city = right_tuple[8]
        past_work = right_tuple[9]
        how_long = right_tuple[-2]
        job_description = right_tuple[-1]
        description = right_tuple[11]

    portal()

    return render_template('index.html', profession=profession, name_surname=name_surname, phone_number=phone_number,
                           email=email, education=education, tech_skills=tech_skills, soft_skills=soft_skills,
                           projects=projects, lang=lang, lang_level=lang_level, country=country, city=city,
                           past_work=past_work, how_long=how_long, job_description=job_description, description=description)

