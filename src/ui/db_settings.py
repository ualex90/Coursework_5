from main import db_creator
from src.head_hunter.api import HeadHunterAPI
from src.ui.ui_utils import UIUtils


def db_settings(utils: UIUtils, employers: dict, api: HeadHunterAPI):
    while True:
        menu_list = ['Создать таблицу "vacancies"',
                     'Создать таблицу "employers"',
                     'Очистить таблицу "vacancies"',
                     'Очистить таблицу "employers"',
                     'Удалить таблицу "vacancies"',
                     'Удалить таблицу "employers"',
                     'Заполнить базу данных',
                     'Назад']
        [print(f"{i + 1}. {menu_list[i]}") for i in range(len(menu_list))]
        match input('>> ').strip():
            case '1':
                utils.clear_screen()
                db_creator.create_table('employers_table.yaml')
            case '2':
                utils.clear_screen()
                db_creator.create_table('vacancies_table.yaml')
            case '3':
                utils.clear_screen()
                db_creator.truncate_table('vacancies')
            case '4':
                utils.clear_screen()
                db_creator.truncate_table('employers')
            case '5':
                utils.clear_screen()
                db_creator.drop_table('vacancies')
            case '6':
                utils.clear_screen()
                db_creator.drop_table('employers')
            case '7':
                utils.clear_screen()
                table_data = api.get_table_data(list(employers.values()))
                db_creator.fill_table(table_data)
            case '8':
                return
