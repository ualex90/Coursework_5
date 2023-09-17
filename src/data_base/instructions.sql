SELECT * FROM employers;
SELECT * FROM vacancies;


SELECT employer_name, area
FROM employers;

SELECT DISTINCT area
FROM employers;

SELECT employer_name
FROM employers
WHERE area = 'Москва';

SELECT employer_id, employer_name
FROM employers
WHERE employer_id BETWEEN 0 AND 9999;

SELECT employer_id, employer_name
FROM employers
WHERE area IN ('Москва', 'Иркутск');

SELECT employer_id, employer_name
FROM employers
WHERE area NOT IN ('Москва', 'Иркутск');

SELECT * FROM employers
ORDER BY employer_name;

SELECT MAX(salary_to)
FROM vacancies;

SELECT * FROM vacancies
WHERE vacancy_name LIKE '%_азработчик%';

SELECT vacancy_name, salary_from, salary_to
FROM vacancies
WHERE salary_from IS NOT NULL or salary_to IS NOT NULL;

SELECT area, COUNT(*)
FROM employers
GROUP BY area
ORDER BY COUNT(*) DESC;

SELECT area, COUNT(*)
FROM employers
GROUP BY area
HAVING COUNT(*) < 4
ORDER BY COUNT(*) DESC;

-- get_companies_and_vacancies_count()
SELECT employer_name, COUNT(*)
FROM employers
JOIN vacancies USING(employer_id)
GROUP BY employer_name;

-- et_all_vacancies()
SELECT vacancies.vacancy_name,
	   employers.employer_name,
	   CONCAT(vacancies.salary_to, ' ', vacancies.currency) AS salary,
	   vacancies.url
FROM vacancies
JOIN employers USING(employer_id)
ORDER BY vacancy_name;