from src.data_base.db_manager import DBManager
from src.ui.ui_utils import UIUtils


def ui_db_manager(utils: UIUtils, db_manager: DBManager):
    """Пользовательский интерфейс DBManager"""
    while True:
        utils.clear_screen()
        menu_list = ['Список всех компаний и количество вакансий у каждой компании',
                     'Список всех вакансий с указанием названия компании',
                     'Средняя зарплата по вакансиям',
                     'Список всех вакансий, у которых зарплата выше средней по всем вакансиям',
                     'Список всех вакансий, в названии которых содержатся ключевые слова',
                     'Назад']
        [print(f"{i + 1}. {menu_list[i]}") for i in range(len(menu_list))]
        match input('>> ').strip():
            case '1':
                data = db_manager.get_companies_and_vacancies_count()
                columns = [('Работодатель', 52), ('Вакансии', 8)]
                utils.create_table(columns, data)
            case '2':
                data = db_manager.get_all_vacancies()
                columns = [('Вакансия', 35), ('Работодатель', 30), ('Зарплата', 12), ('Ссылка на HeadHunter', 30)]
                utils.create_table(columns, data)
            case '3':
                data = db_manager.get_avg_salary()
                columns = [('Средняя зарплата', 16)]
                utils.create_table(columns, data)
            case '4':
                data = db_manager.get_vacancies_with_higher_salary()
                columns = [('Вакансия', 35), ('Работодатель', 30), ('Зарплата', 12), ('Ссылка на HeadHunter', 30)]
                utils.create_table(columns, data)
            case '5':
                utils.clear_screen()
                print('Введите слово или фразу для поиска в названии вакансий')
                keyword = input('>> ').strip()
                data = db_manager.get_vacancies_with_keyword(keyword)
                columns = [('Вакансия', 35), ('Работодатель', 30), ('Зарплата', 12), ('Ссылка на HeadHunter', 30)]
                utils.create_table(columns, data)
            case '6':
                return

