import psycopg2
from psycopg2.errors import DuplicateDatabase

from api_handler.hh_api import HH
from db_handler.config import config


hh = HH()
params = config()


def create_database():
    conn = psycopg2.connect(dbname="hh_vacancies", **params)
    conn.autocommit = True

    cur = conn.cursor()
    try:
        cur.execute("CREATE DATABASE hh_vacancies;")
    except DuplicateDatabase:
        print("Database already exists")

    params.update({"dbname": "hh_vacancies"})


def create_tables():

    with psycopg2.connect(**params) as conn:
        with conn.cursor() as cur:
            cur.execute("DROP TABLE IF EXISTS employers CASCADE;")
            cur.execute("DROP TABLE IF EXISTS vacancies CASCADE;")

            cur.execute("""
                        CREATE TABLE employers (
	                    employer_id serial PRIMARY KEY,
	                    title varchar(100) NOT NULL,
	                    area text,
	                    open_vacancies int,
	                    url text
	                );""")

            cur.execute("""
                        CREATE TABLE vacancies (
	                    vacancy_id serial PRIMARY KEY,
	                    title varchar(100) NOT NULL,
	                    salary_from int,
	                    salary_to int,
	                    description text,
	                    url text,
	                    employer_id int REFERENCES employers(employer_id)
	                );""")
            print("Tables created")
    conn.close()


def insert_into_db_table(employers_list: list):

    with psycopg2.connect(**params) as conn:

        with conn.cursor() as cur:

            cur.execute(f"TRUNCATE TABLE employers, vacancies RESTART IDENTITY;")

            for employer in employers_list:
                emp_values = hh.get_company_by_id(employer)
                cur.execute("INSERT INTO employers VALUES (%s, %s, %s, %s, %s);",
                            (emp_values["employer_id"], emp_values["title"], emp_values["area"], emp_values["open_vacancies"], emp_values["url"]))

            for employer in employers_list:
                vacancies_list = hh.get_vacancies(employer)
                for vacancy in vacancies_list:
                    cur.execute("INSERT INTO vacancies (vacancy_id, title, salary_from, salary_to, description, url, employer_id) VALUES (%s, %s, %s, %s, %s, %s, %s);",
                                (vacancy["id"], vacancy["title"], vacancy["salary_from"], vacancy["salary_to"], vacancy["description"], vacancy["url"], vacancy["employer_id"]))

    conn.close()