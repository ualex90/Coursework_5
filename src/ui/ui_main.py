from src.data_base.db_creator import DBCreator
from src.head_hunter.api import HeadHunterAPI
from src.ui.add_server import add_server
from src.ui.db_settings import db_settings
from src.ui.ui_utils import UIUtils
from src.utils.config import Config

server = dict()


def main_menu():
    while True:
        # Создание объектов для работы с конфигурацией и утилитами UI
        config = Config()
        utils = UIUtils()
        db_creator = None
        employers = config.get_employers()
        api = HeadHunterAPI()
        global server

        # главное меню
        utils.clear_screen()
        menu_list = ['Настройка сервера',
                     'Управление базой данных',
                     'Список работодателей',
                     'Получение данных']
        [print(f"{i + 1}. {menu_list[i]}") for i in range(len(menu_list))]
        match input('>> ').strip():
            case '1':
                utils.clear_screen()
                server = add_server(utils, config)
                db_creator = DBCreator(**server)
            case '2':
                utils.clear_screen()
                if not server:
                    server = add_server(utils, config)
                    db_creator = DBCreator(**server)
                    utils.clear_screen()
                db_settings(utils, employers, api)
            case '3':
                pass


if __name__ == '__main__':
    main_menu()
