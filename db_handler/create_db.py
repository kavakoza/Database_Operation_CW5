import psycopg2

from api_handler.hh_api import HH
from db_handler.config import config

hh = HH
params = config()


def create_tables():

    conn = psycopg2.connect(dbname="hh_vacancies", **params)
    conn.autocommit = True

    with conn.cursor() as cur:
        cur.execute(f"DROP DATABASE hh_vacancies")
        cur.execute(f"CREATE DATABASE hh_vacancies")

    cur.close()
    conn.close()

    with psycopg2.connect(**config()) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                        CREATE TABLE employers (
	                    employer_id int PRIMARY KEY,
	                    title varchar(100) NOT NULL,
	                    area text,
	                    open_vacancies int,
	                    url text
	                )""")

        with conn.cursor() as cur:
            cur.execute("""
                        CREATE TABLE vacancies (
	                    vacancy_id int PRIMARY KEY,
	                    title varchar(100) NOT NULL,
	                    payment int,
	                    description text,
	                    url text,
	                    employer_id int REFERENCES employers(employer_id)
	                )""")

    conn.close()

def insert_into_db_table(employers_list: list):

    with psycopg2.connect(**config()) as conn:

        with conn.cursor() as cur:

            cur.execute(f"TRUNCATE TABLE employers, vacancies RESTART IDENTITY")

            for employer in employers_list:
                emp_values = hh.get_company_by_id(employer)
                cur.execute("INSERT INTO employers VALUES (%s, %s, %s, %s, %s)",
                            (emp_values["employer_id"], emp_values["title"], emp_values["area"], emp_values["open_vacancies"], emp_values["url"]))

            for employer in employers_list:
                vacancies_list = hh.get_vacancies(employer)
                for vacancy in vacancies_list:
                    cur.execute("INSERT INTO vacancies (title, payment, description, url, employer_id) VALUES (%s, %s, %s, %s, %s)",
                                (vacancy["title"], vacancy["payment"], vacancy["description"], vacancy["url"], vacancy["employer_id"]))

        conn.close()