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

-- get_avg_salary()
SELECT CONCAT(ROUND(AVG(salary_to)), ' ', currency)
FROM vacancies
WHERE currency = 'RUR'
GROUP BY currency;

-- get_vacancies_with_higher_salary()
SELECT vacancies.vacancy_name,
	   employers.employer_name,
	   CONCAT(vacancies.salary_to, ' ', vacancies.currency) AS salary,
	   vacancies.url
FROM vacancies
JOIN employers USING(employer_id)
WHERE salary_to > (SELECT AVG(salary_to) FROM vacancies)
ORDER BY salary_to DESC;

-- get_vacancies_with_keyword()
SELECT vacancies.vacancy_name,
	   employers.employer_name,
	   CONCAT(vacancies.salary_to, ' ', vacancies.currency) AS salary,
	   vacancies.url
FROM vacancies
JOIN employers USING(employer_id)
WHERE vacancy_name ILIKE '%КИП%'
ORDER BY vacancy_name;