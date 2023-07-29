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
            SELECT name, open_vacancies
            FROM employers
        """

        return self.cursor_execute(query=query)


    def get_all_vacancies(self):
        query = """
                    SELECT open_vacancies
                    FROM employers
                """

        return self.cursor_execute(query=query)


    def get_average_salary(self):
        query = """
                    SELECT ROUND(AVG(salary_from), ROUND(AVG(salary_to))
                    FROM vacancies
                """

        return self.cursor_execute(query=query)


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
                    WHERE title LIKE "%{keyword}%" OR description LIKE "%{keyword}%"
                """

        return self.cursor_execute(query=query)


