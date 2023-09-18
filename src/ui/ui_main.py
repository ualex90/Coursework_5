from src.data_base.db_creator import DBCreator
from src.data_base.db_manager import DBManager
from src.head_hunter.api import HeadHunterAPI
from src.ui.add_server import db_connect
from src.ui.db_settings import db_settings
from src.ui.employers_list import employers_list
from src.ui.ui_db_manager import ui_db_manager
from src.ui.ui_utils import UIUtils
from src.utils.config import Config

db = dict()
db_creator = DBCreator()
db_manager = DBManager()


def ui_main():
    # Создание объектов для работы с конфигурацией и утилитами UI
    config = Config()
    utils = UIUtils()
    employers = config.get_employers()
    api = HeadHunterAPI()

    while True:
        # главное меню
        global db
        global db_creator
        global db_manager
        utils.clear_screen()
        menu_list = ['Подключение к базе данных',
                     'Управление базой данных',
                     'Список работодателей',
                     'Запросы к базе данных']
        [print(f"{i + 1}. {menu_list[i]}") for i in range(len(menu_list))]
        print('\n(e): Выход из программы')
        match input('>> ').strip():
            case '1':
                utils.clear_screen()
                connect_db(utils, config)
            case '2':
                utils.clear_screen()
                connect_db(utils, config)
                db_settings(utils, db_creator, employers, api)
            case '3':
                utils.clear_screen()
                connect_db(utils, config)
                employers_list(utils, db_creator, config, api)
            case '4':
                utils.clear_screen()
                connect_db(utils, config)
                ui_db_manager(utils, db_manager)
            case 'e':
                return
            case _:
                utils.clear_screen()
                print('Попробуйте еще раз. Необходимо ввести либо номер работодателя, либо (q) для выхода)\n')


def connect_db(utils: UIUtils, config: Config):
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


if __name__ == '__main__':
    ui_main()
