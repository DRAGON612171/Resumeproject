import json

import psycopg2


def rewrite(right):
    a = right.replace('[', '{')
    b = a.replace(']', '}')
    return b


def readTable():
    """ Connect to the PostgreSQL database server """
    conn = psycopg2.connect(
        host="172.17.0.53",
        database="resume_db",
        user="postgres",
        password="kxfs!9E26VGnpzK")
    try:
        print('Connecting to the PostgreSQL database...')

        cur = conn.cursor()

        cur.execute("""SELECT *
                    FROM public.resume_users;""")
        result = cur.fetchall()
        print(result)
        conn.close()
        cur.close()
        return result
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def writeTable(id, name_surname, phone_number, email, education, lang, lang_level, country, city, password, description,
    profession, soft_skills, tech_skills, projects, how_long, job_description, past_work):
    """ Connect to the PostgreSQL database server """
    conn = psycopg2.connect(
        host="172.17.0.53",
        database="resume_db",
        user="postgres",
        password="kxfs!9E26VGnpzK")

    try:
        print('Connecting to the PostgreSQL database...')

        cur = conn.cursor()

        cur.execute("""INSERT INTO public.resume_db(
                                    id, name_surname, phone_number, email, education, lang, lang_level, country, city, password,
                                    description, profession, soft_skills, tech_skills, projects, how_long, job_description, past_work)
                                    VALUES ({}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');""".format(
            id,
            name_surname, phone_number, email, rewrite(json.dumps(education, ensure_ascii=False)),
            rewrite(json.dumps(lang, ensure_ascii=False)), rewrite(json.dumps(lang_level, ensure_ascii=False)),
            country, city, password,
            description, profession, rewrite(json.dumps(soft_skills, ensure_ascii=False)),
            rewrite(json.dumps(tech_skills, ensure_ascii=False)), rewrite(json.dumps(projects, ensure_ascii=False)),
            rewrite(json.dumps(how_long, ensure_ascii=False)), rewrite(json.dumps(job_description, ensure_ascii=False)),
            rewrite(json.dumps(past_work, ensure_ascii=False))))

        conn.commit()
        conn.close()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

