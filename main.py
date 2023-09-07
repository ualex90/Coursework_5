from src.head_hunter.api import HeadHunterAPI
from src.utils.file_manager import FileManager

employers_file = FileManager('employers.yaml')
vacancies_file = FileManager('vacancies.yaml')
api = HeadHunterAPI()

api.get_vacancies(1740)

employers_file.save_file(api.employers)
vacancies_file.save_file(api.vacancies)
