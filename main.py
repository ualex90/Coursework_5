from src.head_hunter.api import HeadHunterAPI
from src.utils.file_manager import FileManager

search_result_file = FileManager('search_result.json')  # Результат поиска работодателей
employer_file = FileManager('employer.yaml')  # информации о работодателе
vacancies_file = FileManager('vacancies.yaml')  # вакансии работодателя
api = HeadHunterAPI()
employer_id = '2'

# Поиск работодателя
search_result_file.save_file(api.get_employers('skypro'))

# Запрос информации о работодателе
employer_file.save_file(api.get_employer_info(employer_id))

# Запрос вакансий работодателя
vacancies_file.save_file(api.get_employer_vacancies(employer_id))


