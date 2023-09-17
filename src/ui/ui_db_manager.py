import math

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
                create_table(utils, columns, data)
            case '2':
                data = db_manager.get_all_vacancies()
                columns = [('Вакансия', 35), ('Работодатель', 30), ('Зарплата', 12), ('Ссылка на HeadHunter', 47)]
                create_table(utils, columns, data)
            case '3':
                pass
            case '4':
                pass
            case '5':
                pass
            case '6':
                return


def create_table(utils, columns: list, data: list):
    """Формирование и вывод в консоль табличных данных"""
    view_page = 0  # просматриваемая страница
    utils.clear_screen()
    while True:
        results = len(data)              # Количество строк
        pages = math.ceil(results / 10)  # Количество страниц
        data_start = view_page * 10      # Индекс элемента для первой строки

        # Количество строк на одной странице
        range_list = 10 if view_page + 1 < pages or results == 10 else results % 10

        # Формирование заголовка
        title_list = [f'{i[0]:^{i[1]}}' for i in columns]
        title = f'|{"№":^7}| {"| ".join(title_list)} |'
        print(f'{title}\n|{"=" * (len(title) - 2)}|')

        # Формирование строк
        for n in range(range_list):
            item = data[data_start]
            string_list = list()
            for i, j in zip(item, columns):
                if isinstance(i, int):
                    string_list.append(f'{i:^{j[1]}}')
                else:
                    string_list.append(f'{(f"{i[:(j[1] - 4)]}..." if len(i) > j[1] else i):<{j[1]}}')
            print(f'|{data_start + 1:^7}| {"| ".join(string_list)} |')
            data_start += 1
        print(f'\nСтраница {view_page + 1} из {pages}')
        print('(q): в меню, (z): назад, (ENTER): вперед\n')

        # Навигация
        user_input = input('>> ').lower().strip()
        if user_input == 'q':
            utils.clear_screen()
            return
        elif user_input == 'z':
            utils.clear_screen()
            view_page -= 1 if view_page > 0 else view_page
        elif user_input == '':
            if pages > view_page + 1:
                utils.clear_screen()
                view_page += 1
            else:
                utils.clear_screen()
        else:
            utils.clear_screen()
            print('Попробуйте еще раз. Необходимо ввести букву навигации\n')
