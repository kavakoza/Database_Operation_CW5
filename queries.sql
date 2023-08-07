CREATE DATABASE hh_vacancies


SELECT title, open_vacancies
FROM employers


SELECT e.title as company, v.title as vacancy_name, v.salary_from as salary_from, v.url as alternate_url
FROM vacancies v
INNER JOIN employers e ON e.employer_id = v.employer_id

SELECT ROUND(AVG(salary_from))
FROM vacancies


SELECT *
FROM vacancies
WHERE salary_from > (SELECT AVG(salary_from) FROM vacancies)


SELECT *
FROM vacancies
WHERE title ILIKE '%{keyword}%' OR description ILIKE '%{keyword}%'