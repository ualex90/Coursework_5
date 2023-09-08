from settings import USER, PASSWORD
from src.data_base.db_creator import DBCreator
from src.head_hunter.api import HeadHunterAPI
from src.utils.config import Config
from src.utils.file_manager import FileManager

search_result_file = FileManager('search_result.json')  # Результат поиска работодателей
employer_file = FileManager('employer.yaml')  # информации о работодателе
vacancies_file = FileManager('vacancies.yaml')  # вакансии работодателя
data_file = FileManager('data.yaml')  # собранные данные о работодателях и их вакансиях
api = HeadHunterAPI()  # Объект для работы с API HeadHunter
config = Config()  # Объект для работы с файлами конфигурации
db_creator = DBCreator('headhunter', USER, PASSWORD)  # Объект для создания базы данных
employer_id = '1740'


# # Поиск работодателя
# search_result_file.save_file(api.get_employers('yandex'))

# # Запрос информации о работодателе
# employer_file.save_file(api.get_employer_info(employer_id))

# # Запрос вакансий работодателя
# vacancies_file.save_file(api.get_employer_vacancies(employer_id))

# # Сохранение работодателей в файл конфигурации
# employers = {"Яндекс": '1740',
#              "Фабрика Решений": '4596113',
#              "Carbon Soft": '1204987',
#              "Группа Компаний РУСАГРО": '23186'}
# config.add_employers(employers)
#
# # Получение работодателей из файла конфигурации
# employers = config.get_employers()

# Добавление данных
# api.add_data('1740')  # "Яндекс"
# api.add_data('4596113')  # "Фабрика Решений"
# api.add_data('1204987')  # "Carbon Soft"
# api.add_data('23186')  # "Группа Компаний РУСАГРО"
# api.add_data(['1740', '4596113', '1204987', '23186'])
# api.add_data(list(employers.values()))
# data_file.save_file(api.data)

# Создание новой базы данных
db_creator.create_db()

