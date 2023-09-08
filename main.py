from src.head_hunter.api import HeadHunterAPI
from src.utils.file_manager import FileManager

search_result_file = FileManager('search_result.json')  # Результат поиска работодателей
employer_file = FileManager('employer.yaml')  # информации о работодателе
vacancies_file = FileManager('vacancies.yaml')  # вакансии работодателя
data_file = FileManager('data.yaml')  # собранные данные о работодателях и их вакансиях
api = HeadHunterAPI()
employer_id = '1204987'

# # Поиск работодателя
# search_result_file.save_file(api.get_employers('yandex'))
#
# # Запрос информации о работодателе
# employer_file.save_file(api.get_employer_info(employer_id))
#
# Запрос вакансий работодателя
vacancies_file.save_file(api.get_employer_vacancies(employer_id))

# # Добавление данных
# api.add_data('1740')  # "Яндекс"
# api.add_data('4596113')  # "Фабрика Решений"
# api.add_data('1204987')  # "Carbon Soft"
# api.add_data('23186')  # "Группа Компаний РУСАГРО"
# data_file.save_file(api.data)
