import psycopg2

from src.data_base.db_manager import DBManager
from src.ui.ui_utils import UIUtils


def ui_db_manager(utils: UIUtils, db_manager: DBManager):
    """Пользовательский интерфейс DBManager"""
    while True:
        menu_list = ['Список всех компаний и количество вакансий у каждой компании',
                     'Список всех вакансий с указанием названия компании',
                     'Средняя зарплата по вакансиям',
                     'Список всех вакансий, у которых зарплата выше средней по всем вакансиям',
                     'Список всех вакансий, в названии которых содержатся ключевые слова']
        [print(f"{i + 1}. {menu_list[i]}") for i in range(len(menu_list))]
        print('\n(q): Назад в главное меню')
        match input('>> ').strip():
            case '1':
                try:
                    data = db_manager.get_companies_and_vacancies_count()
                except psycopg2.errors.UndefinedTable as er:
                    utils.clear_screen()
                    print(f'Таблица не существует. Попробуйте ее создать\n{er}')
                    return True
                else:
                    columns = [('Работодатель', 52), ('Вакансии', 8)]
                    utils.create_table(columns, data)
            case '2':
                try:
                    data = db_manager.get_all_vacancies()
                except psycopg2.errors.UndefinedTable as er:
                    utils.clear_screen()
                    print(f'Таблица не существует. Попробуйте ее создать\n{er}')
                    return True
                else:
                    columns = [('Вакансия', 35), ('Работодатель', 30), ('Зарплата', 12), ('Ссылка на HeadHunter', 30)]
                    utils.create_table(columns, data)
            case '3':
                try:
                    data = db_manager.get_avg_salary()
                except psycopg2.errors.UndefinedTable as er:
                    utils.clear_screen()
                    print(f'Таблица не существует. Попробуйте ее создать\n{er}')
                    return True
                else:
                    columns = [('Средняя зарплата', 16)]
                    utils.create_table(columns, data)
            case '4':
                try:
                    data = db_manager.get_vacancies_with_higher_salary()
                except psycopg2.errors.UndefinedTable as er:
                    utils.clear_screen()
                    print(f'Таблица не существует. Попробуйте ее создать\n{er}')
                    return True
                else:
                    columns = [('Вакансия', 35), ('Работодатель', 30), ('Зарплата', 12), ('Ссылка на HeadHunter', 30)]
                    utils.create_table(columns, data)
            case '5':
                utils.clear_screen()
                print('Введите слово или фразу для поиска в названии вакансий')
                keyword = input('>> ').strip()
                try:
                    data = db_manager.get_vacancies_with_keyword(keyword)
                except psycopg2.errors.UndefinedTable as er:
                    utils.clear_screen()
                    print(f'Таблица не существует. Попробуйте ее создать\n{er}')
                    return True
                else:
                    columns = [('Вакансия', 35), ('Работодатель', 30), ('Зарплата', 12), ('Ссылка на HeadHunter', 30)]
                    utils.create_table(columns, data)
            case 'q':
                return
            case _:
                utils.clear_screen()
                print('Попробуйте еще раз. Необходимо ввести либо номер работодателя, либо (q) для выхода)\n')

