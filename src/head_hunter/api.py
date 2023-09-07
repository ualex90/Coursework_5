import requests


class HeadHunterAPI:
    def __init__(self):
        self.employers = list()
        self.vacancies = list()

    @staticmethod
    def get_employers(text):
        url = 'https://api.hh.ru/employers'
        params = {'text': text}
        response = requests.get(url, params=params).json()
        return response

    def get_employer_info(self, employer_id):
        url = f'https://api.hh.ru/employers/{employer_id}'
        params = {}
        response = requests.get(url, params=params).json()
        self.employers.append(response)
        return response

    def get_vacancies(self, employer_id, page=None, per_page=50, page_limit=None) -> dict:
        """
        Возвращает список вакансий по запросу.
        Можно за раз получить не более 2000 вакансий

        :param employer_id: ID работодателя
        :param page: Страница ответа
        :param per_page: Количество вакансий на странице (не более 50)
        :param page_limit: Максимальное количество страниц (максимум 40 при per_page=50)
        :return:
        """
        employer_info = self.get_employer_info(employer_id)

        # Инициализация запроса
        print(f'Запрос вакансий "{employer_info.get("name")}"')

        url = 'https://api.hh.ru/vacancies'
        params = {'employer_id': employer_id,
                  'page': page,
                  'per_page': per_page
                  }
        response = requests.get(url, params=params).json()

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
                    response = requests.get(url, params).json()
                    vacancies.extend(response.get('items'))
                    response['page'] += 1
                    params["page"] += 1
                print(f'\r"{employer_info.get("name")}" - Ok                                        ')
            else:
                vacancies = response.get('items')
                print(f'\r"{employer_info.get("name")}" - Ok                                        ')
        else:
            print(f'"{employer_info.get("name")}" - Вакансии отсутствуют')
        self.vacancies.append(vacancies)
        # Возврат нормализованного списка
        # return self.normalization_data(vacancies)


if __name__ == '__main__':
    x = HeadHunterAPI()
    x.get_vacancies(1740)

