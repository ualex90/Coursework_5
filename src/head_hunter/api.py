import requests


class HeadHunterAPI:
    def __init__(self):
        self.employer_info = dict()
        self.vacancies = list()

    @staticmethod
    def request_data(url, params, headers=None):
        response = requests.get(url, headers=headers, params=params).json()
        return response

    def get_employers(self, text: str) -> dict:
        """Поиск работодателей"""
        url = 'https://api.hh.ru/employers'
        params = {'text': text}
        return self.request_data(url, params)

    def get_employer_info(self, employer_id: str) -> dict:
        """Получение информации о работодателе"""
        url = f'https://api.hh.ru/employers/{employer_id}'
        params = {}
        data = self.request_data(url, params)
        self.employer_info = data
        return data if data is not None else dict()

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
        if not employer_info.get('open_vacancies'):
            print(f'"{employer_info.get("name")}" - отсутствуют активные вакансии')
            return list()

        # Инициализация запроса
        print(f'Запрос вакансий "{employer_info.get("name")}"')

        url = 'https://api.hh.ru/vacancies'
        params = {'employer_id': employer_id,
                  'page': page,
                  'per_page': per_page
                  }
        response = self.request_data(url, params)

        # Определение максимального количества страниц
        if page_limit is None or page_limit > response.get('pages'):
            page_limit = response.get('pages')

        # Перебор страниц и получение данных
        vacancies = list()
        if response.get('pages'):
            if page is None:
                params["page"] = 0
                while response.get('page') < page_limit:
                    print(f'\rПолучение данных (станица {params["page"] + 1} из {page_limit})', end='')
                    response = self.request_data(url, params)
                    vacancies.extend(response.get('items'))
                    response['page'] += 1
                    params["page"] += 1
                print(f'\r"{employer_info.get("name")}" - Ok                                        ')
            else:
                vacancies = response.get('items')
                print(f'\r"{employer_info.get("name")}" - Ok                                        ')
        else:
            print(f'"{employer_info.get("name")}" - Вакансии отсутствуют')
        self.vacancies = vacancies
        return vacancies if vacancies is not None else list()


if __name__ == '__main__':
    x = HeadHunterAPI()
    x.get_employer_vacancies('1740')
