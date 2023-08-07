import psycopg2

from db_handler.config import config


class DBManager:

    params = config()
    connection = psycopg2.connect(dbname="hh_vacancies", **params)

    def cursor_execute(self, query: str) -> list:
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()


    def disconnect(self):
        self.connection.close()


    def get_companies_and_vacancies(self):
        query = """
            SELECT title, open_vacancies
            FROM employers
        """

        return self.cursor_execute(query=query)


    def get_all_vacancies(self):
        query = """
                    SELECT e.title as company, v.title as vacancy_name, v.salary_from as salary_from, v.url as alternate_url
                    FROM vacancies v
                    INNER JOIN employers e ON e.employer_id = v.employer_id                    
                """

        return self.cursor_execute(query=query)


    def get_average_salary(self):
        query = """
                    SELECT ROUND(AVG(salary_from))
                    FROM vacancies
                """

        return self.cursor_execute(query=query)[0][0]


    def get_vacancies_with_higher_salary(self):
        query = """
                    SELECT *
                    FROM vacancies
                    WHERE salary_from > (SELECT AVG(salary_from) FROM vacancies)
                """

        return self.cursor_execute(query=query)


    def get_vacancies_with_keyword(self, keyword: str):
        query = f"""
                    SELECT *
                    FROM vacancies
                    WHERE title ILIKE '%{keyword}%' OR description ILIKE '%{keyword}%'
                """

        return self.cursor_execute(query=query)


