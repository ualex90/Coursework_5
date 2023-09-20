from src.data_base.db_creator import DBCreator
from src.data_base.db_manager import DBManager
from src.head_hunter.api import HeadHunterAPI
from src.ui.add_server import db_connect
from src.ui.db_settings import db_settings
from src.ui.employers_list import employers_list
from src.ui.ui_db_manager import ui_db_manager
from src.ui.ui_utils import UIUtils
from src.utils.config import Config

# Создание объектов для работы с конфигурацией и утилитами UI
db = dict()
db_creator = DBCreator()
db_manager = DBManager()
api = HeadHunterAPI()
config = Config()
utils = UIUtils()
employers = config.get_employers()


def ui_main():
    while True:
        # главное меню
        global db
        global db_creator
        global db_manager
        utils.clear_screen()
        menu_list = ['Подключение к базе данных',
                     'Редактировать списка работодателей',
                     'Управление базой данных',
                     'Запросы к базе данных']
        [print(f"{i + 1}. {menu_list[i]}") for i in range(len(menu_list))]
        print('\n(e): Выход из программы')
        match input('>> ').strip():
            case '1':
                utils.clear_screen()
                connect_db()
                utils.clear_screen()
            case '2':
                utils.clear_screen()
                connect_db()
                utils.clear_screen()
                if employers_list(utils, db_creator, config, api):
                    create_db()
            case '3':
                utils.clear_screen()
                connect_db()
                utils.clear_screen()
                db_settings(utils, db_creator, employers, api)
            case '4':
                utils.clear_screen()
                connect_db()
                utils.clear_screen()
                if ui_db_manager(utils, db_manager):
                    create_db()
                    ui_db_manager(utils, db_manager)
            case 'e':
                utils.clear_screen()
                return
            case _:
                utils.clear_screen()
                print('Попробуйте еще раз. Необходимо ввести либо номер работодателя, либо (q) для выхода)\n')


def connect_db():
    global db
    global db_creator
    global db_manager
    if not db:
        db = db_connect(utils, config)
        db_creator = DBCreator(**db)
        db_manager = DBManager(**db)
        utils.clear_screen()
        print("Попытка соединения...")
        if not db_creator.create_db():
            input('Ошибка соединения. Нажмите "ENTER"')
        else:
            message = f'Соединение с базой данных {config.get_server()["db_name"]} установлено'
            print(message)
            print('-' * len(message))
            input('Нажмите "ENTER"')


def create_db():
    answer = input(f'Создать базу данных? (y/n) ')
    if answer.strip().lower() == 'y' or answer.strip().lower() == 'д':
        db_creator.create_db()
        db_creator.truncate_table('employers')
        db_creator.create_table('employers_table.yaml')
        db_creator.truncate_table('vacancies')
        db_creator.create_table('vacancies_table.yaml')
        table_data = api.get_table_data(list(employers.values()))
        db_creator.fill_table(table_data)
        return


if __name__ == '__main__':
    ui_main()
