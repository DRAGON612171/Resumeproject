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
    how_long = ''
    job_description = ''
    user_id = ''
    rand_password = ''
    description = ''

    def portal():
        nonlocal name_surname, phone_number, email, education, tech_skills, soft_skills, projects, lang, lang_level, \
                            country, city, past_work, description, profession, how_long, job_description
        result = readTable()
        name_surname = result[0][1]
        phone_number = result[0][2]
        email = result[0][3]
        education = result[0][4]
        lang = result[0][5]
        lang_level = result[0][6]
        country = result[0][7]
        city = result[0][8]
        description = result[0][10]
        profession = result[0][11]
        past_work = result[0][-1]
        job_description = result[0][-2]
        how_long = result[0][-3]
        projects = result[0][-4]
        tech_skills = result[0][-5]
        soft_skills = result[0][-6]

    def another_past_work():
        return """<div>
                    <h4 class="pst_wrk">{{past_work}}</h4>
                    {% for a in range( how_long | length ) %}
                    <p>{{how_long[a]}}</p>
                    {% endfor %}
                    <ul class='pst_wrk_list'>
                        {% for i in range(job_description | length) %}
                        <li class="li"> <span>{{job_description[i]}}</span></li>
                        {% endfor %}
                    </ul>
                </div>"""

    portal()
    return render_template('index.html', profession=profession, name_surname=name_surname, phone_number=phone_number,
                           email=email, education=education, tech_skills=tech_skills, soft_skills=soft_skills,
                           projects=projects, lang=lang, lang_level=lang_level, country=country, city=city,
                           past_work=past_work, how_long=how_long, job_description=job_description, description=description)

