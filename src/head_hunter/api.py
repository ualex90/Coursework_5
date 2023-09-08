import requests


class HeadHunterAPI:
    """Получение данных о работодателях и их вакансиях"""
    def __init__(self):
        self.__employers_id = list()
        self.__data = list()

    @property
    def data(self):
        """Сведения о работодателях и их вакансиях"""
        return self.__data

    @property
    def employers_id(self):
        """Список добавленных работодателей"""
        return self.__employers_id

    @staticmethod
    def data_request(url, params, headers=None):
        """Запрос данных"""
        response = None
        try:
            response = requests.get(url, headers=headers, params=params).json()
        except requests.exceptions.ConnectionError:
            print('Сервер не доступен')
            return None
        return response

    def add_data(self, employer_id):
        """
        Добавление данных о работодателях и их вакансиях
        Метод исключает повторное добавление работодателя
        """
        employer = self.get_employer_info(employer_id)
        vacancies = self.get_employer_vacancies(employer_id)
        if employer:
            if employer_id not in self.__employers_id:
                self.__data.append({'employer': employer, 'vacancies': vacancies})
                self.__employers_id.append(employer_id)

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

    def get_employer_vacancies(self, employer_id: str, page=None, per_page=50, page_limit=None) -> list:
        """
        Возвращает список вакансий по запросу.
        Можно за раз получить не более 2000 вакансий

        :param employer_id: ID работодателя
        :param page: Страница ответа
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
                  'page': page,
                  'per_page': per_page
                  }
        response = self.data_request(url, params)

        # Определение максимального количества страниц
        if page_limit is None or page_limit > response.get('pages'):
            page_limit = response.get('pages')

        # Перебор страниц и получение данных
        vacancies = list()
        if page is None:
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

    def __str__(self):
        return f'Содержит {len(self.__data)} записей о работодателях'


if __name__ == '__main__':
    x = HeadHunterAPI()
    x.get_employer_vacancies('1740')
