import math

from src.data_base.db_creator import DBCreator
from src.head_hunter.api import HeadHunterAPI
from src.ui.ui_utils import UIUtils
from src.utils.config import Config


def employers_list(utils: UIUtils, db_creator: DBCreator, config: Config, api: HeadHunterAPI):
    """Список работодателей"""
    view_page = 0  # просматриваемая страница
    utils.clear_screen()
    employers_old = config.get_employers()
    while True:
        employers = config.get_employers()  # Словарь с работодателями и их ID
        items = list(employers)             # Список из работодателей
        results = len(employers)            # Количество работодателей
        count = 0                           # Счетчик строк таблицы
        pages = math.ceil(results / 10)     # Количество страниц
        item_start = view_page * 10  # Индекс элемента для первой строки

        # Количество строк на одной странице
        range_list = 10 if view_page + 1 < pages or results == 10 else results % 10

        print("|№|   ID    |                                  КОМПАНИЯ                                         |\n"
              "|===============================================================================================|")
        for i in range(range_list):
            item = items[item_start]
            emp_name = f"{item[:15]}..." if len(item) > 80 else item
            print(f"|{count}| {employers[item]:<8} | {emp_name:<80} |")
            count += 1
            item_start += 1
        print(f'\nСтраница {view_page + 1} из {pages}')
        print('(q): в меню, (z): назад, (ENTER): вперед\n'
              'Для добавления работодателя введите (a)\n'
              'Для удаления работодателя из списка введите его номер.')

        user_input = input('>> ').lower().strip()
        if user_input.isdigit() and len(user_input) == 1:
            if int(user_input) <= range_list - 1:
                item = items[view_page * 10 + int(user_input)]
                utils.clear_screen()
                answer = input(f'Вы уверены что хотите удалить "{item}"? (y/n) ')
                if answer.strip().lower() == 'y' or answer.strip().lower() == 'д' or answer.strip().lower() == '':
                    del employers[item]
                    config.save_employers(employers)
            else:
                utils.clear_screen()
                print("Введите номер работодателя из списка")
        elif user_input == 'a':
            utils.clear_screen()
            print('Введите ID работодателей через запятую')
            emp_id = input('>> ').strip()
            emp_id_list = list(map(lambda x: x.strip(), emp_id.split(',')))
            for item in emp_id_list:
                data = api.get_employer_info(item)
                if data.get('name'):
                    employers.update({data['name']: data['id']})
            config.add_employers(employers)
        elif user_input == 'q':
            utils.clear_screen()
            config.add_employers(employers)
            if employers_old == employers:
                return
            else:
                answer = input(f'Записать изменения в базу данных (y/n) ')
                if answer.strip().lower() == 'y' or answer.strip().lower() == 'д' or answer.strip().lower() == '':
                    db_creator.create_db()
                    db_creator.truncate_table('vacancies')
                    db_creator.truncate_table('employers')
                    db_creator.create_table('vacancies_table.yaml')
                    db_creator.create_table('employers_table.yaml')
                    table_data = api.get_table_data(list(employers.values()))
                    db_creator.fill_table(table_data)
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
            print('Попробуйте еще раз. Необходимо ввести либо номер работодателя, либо букву навигации\n')
