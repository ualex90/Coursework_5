from settings import USER, PASSWORD
from src.data_base.db_creator import DBCreator
from src.head_hunter.api import HeadHunterAPI
from src.utils.config import Config
from src.utils.file_manager import FileManager

api = HeadHunterAPI()  # Объект для работы с API HeadHunter
config = Config()  # Объект для работы с файлами конфигурации

# -------------------------------Формирование запросов API и сохранение данных------------------------------------------

search_result_file = FileManager('search_result.json')  # Результат поиска работодателей
employer_file = FileManager('employer.yaml')  # информации о работодателе
vacancies_file = FileManager('vacancies.yaml')  # вакансии работодателя
data_file = FileManager('data.yaml')  # собранные данные о работодателях и их вакансиях
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
# Получение работодателей из файла конфигурации
employers = config.get_employers()

# Добавление данных в api.data
# table_data = api.get_table_data('1740')  # "Яндекс"
# table_data = api.get_table_data('4596113')  # "Фабрика Решений"
# table_data = api.get_table_data('1204987')  # "Carbon Soft"
# table_data = api.get_table_data('23186')  # "Группа Компаний РУСАГРО"
# table_data = api.get_table_data(['1740', '4596113', '1204987', '23186'])
table_data = api.get_table_data(list(employers.values()))
# data_file.save_file(table_data)

# -------------------------------Создание и удаление базы данных и ее таблиц--------------------------------------------

db_creator = DBCreator('headhunter', USER, PASSWORD)  # Объект для создания базы данных

# Создание новой базы данных
# db_creator.create_db()

# Создание новой таблицы
# db_creator.create_table('employers_table.yaml')
# db_creator.create_table('vacancies_table.yaml')

# # Удаление данных из таблицы
# db_creator.truncate_table('vacancies')
# db_creator.truncate_table('employers')
#
# # Удаление таблицы
# db_creator.drop_table('vacancies')
# db_creator.drop_table('employers')

# -----------------------------------------Заполнение таблиц данными----------------------------------------------------

# заполнение таблиц данными
db_creator.fill_table(table_data)
