import psycopg2


def readTable():
    """ Connect to the PostgreSQL database server """
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="resume_db",
        user="postgres",
        password="464254")
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


def writeTable(id, name_surname, phone_number, email, education, skills, projects, lang, lang_level, country, city, past_work, password, description, profession):
    """ Connect to the PostgreSQL database server """
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="resume_db",
        user="postgres",
        password="464254")
    try:
        print('Connecting to the PostgreSQL database...')

        cur = conn.cursor()

        cur.execute('''INSERT INTO public.resume_users(
                   id, name, surname, phone_number, email, education, skills,
                   projects, lang, lang_level, country, city, past_work, password, description, profession)
                   VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {});'''.format(id, name_surname, phone_number, email, education, skills, projects, lang, lang_level, country, city, past_work, password, description, profession))

        conn.commit()
        conn.close()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

