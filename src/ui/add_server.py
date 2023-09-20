from src.data_base.db_creator import DBCreator
from src.ui.ui_utils import UIUtils
from src.utils.config import Config


def db_connect(utils: UIUtils, config: Config) -> dict:
    """Получение данных о сервере"""
    server = config.get_server()

    # получение данных сохраненного сервера
    if tuple(server.keys()) == ('host', 'port', 'user', 'password', 'db_name'):
        answer = input(f'Подключиться к введенному ранее серверу "{server["host"]}:{server["port"]}, '
                       f'{server["user"]}"? (y/n) ')
        if answer.strip().lower() == 'y' or answer.strip().lower() == 'д' or answer.strip().lower() == '':
            return server

    # получение данных от пользователя
    utils.clear_screen()
    warning = "Для работы с программой необходимо знать данные для подключения к серверу базы данных PosgreSQL!!!"
    print(f'{warning}\n{"-" * (len(warning))}')
    print('Введите адрес сервера или нажмите "ENTER" если "localhost')
    host = input("Адрес: ").strip().lower()
    if not host:
        host = "localhost"
    utils.clear_screen()

    print('Введите порт или нажмите "ENTER" если "5432"')
    port = input("Порт: ").strip().lower()
    if not port:
        port = "5432"
    utils.clear_screen()

    user = str()
    while not user:
        user = input('Имя пользователя: ').strip()
        if not user:
            utils.clear_screen()
            print('Имя пользователя не должно быть пустым, попробуйте ввести еще раз')
    utils.clear_screen()

    password = input('Пароль: ')
    utils.clear_screen()

    print('Введите имя для базы данных для HeadHunter (по умолчанию "headhunter")')
    db_name = input("Имя базы данных: ").strip().lower()
    if not db_name:
        db_name = "headhunter"
    utils.clear_screen()

    data = {'host': host, 'port': port, 'user': user, 'password': password, 'db_name': db_name}
    config.add_server(data)
    return data
