import psycopg2

from src.data_base.db import DB


class DBManager(DB):

    def _request(self, instruction):
        conn = self.connection()
        response = dict()
        if conn:
            try:
                with conn:
                    with conn.cursor() as cursor:
                        cursor.execute(instruction)
                        response = cursor.fetchall()
            finally:
                conn.close()
        return response

    def get_companies_and_vacancies_count(self):
        """
        Получает список всех компаний и количество вакансий
        у каждой компании
        """
        instruction = 'SELECT * FROM employers'
        print(self._request(instruction))

    def get_all_vacancies(self):
        """
        Получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию
        """
        pass

    def get_avg_salary(self):
        """
        Получает среднюю зарплату по вакансиям
        """
        pass

    def get_vacancies_with_higher_salary(self):
        """
        Получает список всех вакансий, у которых зарплата выше
        средней по всем вакансиям
        """
        pass

    def get_vacancies_with_keyword(self, keyword: str):
        """
        Получает список всех вакансий, в названии которых содержатся
        переданные в метод слова, например python
        """
        pass

