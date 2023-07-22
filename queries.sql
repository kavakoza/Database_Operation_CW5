CREATE DATABASE hh_vacancies


SELECT name, open_vacancies
FROM employers


SELECT open_vacancies
FROM employers


SELECT ROUND(AVG(salary_from), ROUND(AVG(salary_to))
FROM vacancies


SELECT *
FROM vacancies
WHERE salary_from > (SELECT AVG(salary_from) FROM vacancies)


SELECT *
FROM vacancies
WHERE title LIKE "%{keyword}%" OR description LIKE "%{keyword}%"