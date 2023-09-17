import requests


class HeadHunterAPI:
    """Получение данных о работодателях и их вакансиях"""

    @staticmethod
    def data_request(url, params, headers=None):
        """Запрос данных"""
        try:
            response = requests.get(url, headers=headers, params=params).json()
        except requests.exceptions.ConnectionError:
            print('Сервер не доступен')
            return None
        return response

    def get_employers(self, text: str) -> dict:
        """Поиск работодателей"""
        url = 'https://api.hh.ru/employers'
        params = {'text': text}
        return self.data_request(url, params)

    def get_employer_info(self, employer_id: str) -> dict:
        """Получение информации о работодателе"""
        url = f'https://api.hh.ru/employers/{employer_id}'
        params = {}
        data = self.data_request(url, params)
        if data is None:
            return dict()
        return data

    def get_employer_vacancies(self, employer_id: str, per_page=50, page_limit=None) -> list:
        """
        Возвращает список вакансий по запросу.
        Можно за раз получить не более 2000 вакансий

        :param employer_id: ID работодателя
        :param per_page: Количество вакансий на странице (не более 50)
        :param page_limit: Максимальное количество страниц (максимум 40 при per_page=50)
        :return:
        """

        # Получение данных о работодателе и проверка на наличии открытых вакансий
        employer_info = self.get_employer_info(employer_id)
        if not employer_info.get("name"):
            return list()
        if not employer_info.get('open_vacancies'):
            print(f'"{employer_info.get("name")}" - отсутствуют активные вакансии')
            return list()

        url = 'https://api.hh.ru/vacancies'
        params = {'employer_id': employer_id,
                  'per_page': per_page
                  }
        response = self.data_request(url, params)

        # Определение максимального количества страниц
        if page_limit is None or page_limit > response.get('pages'):
            page_limit = response.get('pages')

        # Перебор страниц и получение данных
        vacancies = list()
        if response.get('pages') > 1:
            params["page"] = 0
            while response.get('page') < page_limit:
                print(f'\r"{employer_info.get("name")}" - (станица {params["page"] + 1} из {page_limit})', end='')
                response = self.data_request(url, params)
                vacancies.extend(response.get('items'))
                response['page'] += 1
                params["page"] += 1
            print(f'\r"{employer_info.get("name")}" - Получено {len(vacancies)} вакансий                 ')
        else:
            vacancies = response.get('items')
            print(f'\r"{employer_info.get("name")}" - Получено {len(vacancies)} вакансий                 ')
        return vacancies if vacancies is not None else list()

    def get_table_data(self, employers_id) -> list:
        """
        Получение табличных данных о работодателях и их вакансиях
        Метод исключает повторное добавление работодателя

        :param employers_id: ID работодателей. Одного в формате str, или нескольких list[str]
        """
        # Проверка типа данных аттрибута employers_id
        employers_list = list()
        if isinstance(employers_id, str):
            employers_list.append(employers_id)
        elif isinstance(employers_id, list):
            employers_list = employers_id
        else:
            raise TypeError("The data must be of type str or list[str]")

        # Получение табличных данных и сборка их в единый список
        table_data = list()
        employers_id = list()
        for employer_id in employers_list:
            employer = self.get_employer_info(employer_id)
            vacancies = self.get_employer_vacancies(employer_id, page_limit=None)
            if employer:
                if employer_id not in employers_id:
                    employers_id.append(employer_id)
                    table_data.append(self.normalize_data(employer, vacancies))
        return table_data

    @staticmethod
    def normalize_data(employer: dict, vacancies: list) -> dict:
        """
        Выборка полученных данных по API и формирование нормализованного
        словаря содержащего работодателя и его вакансий
        """
        # формирование табличных данных работодателя
        employer_tab = [{'employer_id': int(employer.get('id')),
                         'employer_name': employer.get('name'),
                         'area': employer.get('area').get('name'),
                         'site_url': employer.get('site_url'),
                         'description': employer.get('description')}]

        # формирование табличных данных вакансий работодателя
        vacancies_tab = list()
        for vacancy in vacancies:
            salary_from = None
            salary_to = None
            if vacancy.get('salary'):
                if vacancy.get('salary').get('from') and vacancy.get('salary').get('to'):
                    salary_from = int(vacancy.get('salary').get('from'))
                    salary_to = int(vacancy.get('salary').get('to'))
                elif vacancy.get('salary').get('from'):
                    salary_from = int(vacancy.get('salary').get('from'))
                    salary_to = salary_from
                elif vacancy.get('salary').get('to'):
                    salary_to = int(vacancy.get('salary').get('to'))
                    salary_from = salary_to
                else:
                    salary_from = None
                    salary_to = None
            vacancies_tab.append({'vacancy_id': int(vacancy.get('id')),
                                  'employer_id': int(employer.get('id')),
                                  'employer_name': vacancy.get('name'),
                                  'area': vacancy.get('area').get('name'),
                                  'salary_from': salary_from,
                                  'salary_to': salary_to,
                                  'currency': vacancy.get('salary').get('currency') if vacancy.get('salary') else None,
                                  'url': vacancy.get('url'),
                                  'requirement': vacancy.get('snippet').get('requirement'),
                                  'responsibility': vacancy.get('snippet').get('responsibility')
                                  })
        return {'employers': employer_tab, 'vacancies': vacancies_tab}

    def __str__(self):
        return f'Объект для работы с API HeadHunter'


if __name__ == '__main__':
    x = HeadHunterAPI()
    x.get_employer_vacancies('1740')
