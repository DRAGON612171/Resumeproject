import psycopg2
import sshtunnel


def rewrite(right):
    a = []
    for lab in range(len(right)):
        a = '"{0}"'.format(right[lab])
    return a


id = 2345353453
name_surname = 'Roma'
phone_number = '38050000000'
email = 'Email'
education = ('Garvard', 'Oxford')
lang = ('eng', 'ukr')
lang_level = ('B2', 'C2')
country ='Ukraine'
city = 'KYIV'
password = 'KEOFNkdsf'
description = 'Хочу робити шштучний інтелект'
profession = 'Python Developer'
soft_skills = ('1', '2', '3')
tech_skills = ('SQl', 'data base')
projects = ('link_1', 'link_2')
how_long = ('Чеврень 2021 - Лютий 2022', 'Грудень 2009 - Січень 2010')
job_description = ('бази даних', 'Створював таблички')
past_work = ('Python Developer', 'SQL Deveper')


def writeTable(id, name_surname, phone_number, email, education, lang, lang_level, country, city, password, description,
    profession, soft_skills, tech_skills, projects, how_long, job_description, past_work):
    sshtunnel.SSH_TIMEOUT = 10.0
    sshtunnel.TUNNEL_TIMEOUT = 10.0
    postgres_hostname = "goiteens-3055.postgres.pythonanywhere-services.com"
    postgres_host_port = 13055
    try:
        with sshtunnel.SSHTunnelForwarder(('ssh.pythonanywhere.com'),
                ssh_username='goiteens',
                ssh_password='productionteam123',
                remote_bind_address=(postgres_hostname, postgres_host_port)) as tunnel:
            connection = psycopg2.connect(
                user='super', password='kxfs!9E26VGnpzK',
                host='127.0.0.1', port=tunnel.local_bind_port,
                database='postgres')
            cur = connection.cursor()

            cur.execute("""INSERT INTO public.resume_db(
                            id, name_surname, phone_number, email, education, lang, lang_level, country, city, password,
                            description, profession, soft_skills, tech_skills, projects, how_long, job_description, past_work)
                            VALUES ({}, '{}', '{}', '{}', {}, {}, {}, '{}', '{}', '{}', '{}', '{}', {}, {}, {}, {}, {}, {});""".format(id,
                            name_surname, phone_number, email, education, lang, lang_level,
                            country, city, password,
                            description, profession, soft_skills, tech_skills, projects,
                            how_long, job_description, past_work))

            connection.commit()
            connection.close()
            cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def readTable():
    sshtunnel.SSH_TIMEOUT = 10.0
    sshtunnel.TUNNEL_TIMEOUT = 10.0
    postgres_hostname = "goiteens-3055.postgres.pythonanywhere-services.com"
    postgres_host_port = 13055
    try:
        with sshtunnel.SSHTunnelForwarder(('ssh.pythonanywhere.com'),
                ssh_username='goiteens',
                ssh_password='productionteam123',
                remote_bind_address=(postgres_hostname, postgres_host_port)) as tunnel:
            connection = psycopg2.connect(
                user='super', password='kxfs!9E26VGnpzK',
                host='127.0.0.1', port=tunnel.local_bind_port,
                database='postgres')
            cur = connection.cursor()
            cur.execute("""SELECT *
            FROM public.resume_db;""")
            result = cur.fetchall()
            print(result)
            connection.close()
            cur.close()
            return result
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


writeTable(id, name_surname, phone_number, email, education, lang, lang_level, country, city, password, description,
    profession, soft_skills, tech_skills, projects, how_long, job_description, past_work)