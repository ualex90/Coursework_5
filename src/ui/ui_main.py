from src.data_base.db_creator import DBCreator
from src.head_hunter.api import HeadHunterAPI
from src.ui.add_server import db_connect
from src.ui.db_settings import db_settings
from src.ui.employers_list import employers_list
from src.ui.ui_utils import UIUtils
from src.utils.config import Config

db = dict()
db_creator = None


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
        utils.clear_screen()
        menu_list = ['Подключение к базе данных',
                     'Управление базой данных',
                     'Список работодателей',
                     'Получение данных',
                     'Выход из программы']
        [print(f"{i + 1}. {menu_list[i]}") for i in range(len(menu_list))]
        match input('>> ').strip():
            case '1':
                utils.clear_screen()
                db = db_connect(utils, config)
                db_creator = DBCreator(**db)
                utils.clear_screen()
                print("Попытка соединения...")
                if not db_creator.create_db():
                    input('Ошибка соединения. Нажмите "ENTER"')
                else:
                    message = f'Соединение с базой данных {config.get_server()["db_name"]} установлено'
                    print(message)
                    print('-' * len(message))
                    input('Нажмите "ENTER"')
            case '2':
                utils.clear_screen()
                connect_db(utils, config)
                db_settings(utils, db_creator, employers, api)
            case '3':
                utils.clear_screen()
                connect_db(utils, config)
                employers_list(utils, db_creator, config, api)
            case '4':
                pass
            case '5':
                utils.clear_screen()
                return


def connect_db(utils: UIUtils, config: Config):
    global db
    global db_creator
    if not db:
        db = db_connect(utils, config)
        db_creator = DBCreator(**db)
        if not db_creator.create_db():
            input('Ошибка соединения. Нажмите "ENTER')
        utils.clear_screen()


if __name__ == '__main__':
    ui_main()
