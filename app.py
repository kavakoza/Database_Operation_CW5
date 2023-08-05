from api_handler.constants import employers_list
from db_handler.db_manager import DBManager
from db_handler.create_db import *

dbmanager = DBManager()

def user_interaction():

    create_database()
    create_tables()
    insert_into_db_table(employers_list)


    while True:

        print('Welcome to the Job Finder!\n'
              'Choose an option:\n'
              '1 - List of all companies and available vacancies\n'
              '2 - List of all vacancies\n'
              '3 - Average salary\n'
              '4 - List of vacancies with salary higher than average\n'
              '5 - List of vacancies with a keyword\n'
              '0 - Exit')

        search_query = input('Enter option number: ')

        if search_query == '1':
            #List of all companies and available vacancies
            companies_vacancies = dbmanager.get_companies_and_vacancies()
            print("List of all companies and available vacancies:")
            for company, vacancies in companies_vacancies:
                print(f"Company: {company} has available vacancies: {vacancies}")
            print()

        elif search_query == '2':
            #List of all vacancies
            all_vacancies = dbmanager.get_all_vacancies()
            print("List of all vacancies:")
            for company, vacancy_name, salary_from, alternate_url in all_vacancies:
                print(f"Company: {company}, Vacancy: {vacancy_name}, Salary: {salary_from}, Link: {alternate_url}")
            print()


        elif search_query == '3':
            #Average salary
            average_salary = dbmanager.get_average_salary()
            print(average_salary)
            print(f"Average salary:{round(average_salary)}")
            print()


        elif search_query == '4':
            #List of vacancies with salary higher than average
            high_salary_vacancies = dbmanager.get_vacancies_with_higher_salary()
            print("List of vacancies with salary higher than average:")
            for vacancy in high_salary_vacancies:
                print(vacancy)
            print()


        elif search_query == '5':
            #List of vacancies with a keyword
            keyword = input('Enter a keyword: ')
            keyword_vacancies = dbmanager.get_vacancies_with_keyword(keyword)
            print("List of vacancies with a keyword:")
            for vacancy in keyword_vacancies:
                print(vacancy)
            print()


        elif search_query == '0':
            print('See you next time!')
            break


        else:
            print('Wrong option. Choose a number from the list.')

    #Close db connection
    dbmanager.disconnect()


if __name__ == '__main__':
    user_interaction()