import psycopg2
from pathlib import Path

from settings import TABLES
from src.utils.file_manager import FileManager


class DBCreator:
    """Создание базы данных"""

    def __init__(self, db_name: str, user: str, password: str, host='localhost', port='5432') -> None:
        """
        Инициализация

        :param db_name: Имя базы данных с которой предстоит работать далее
        :param user: Имя пользователя
        :param password: Пароль
        :param host: Адрес сервера
        :param port: Порт сервера
        """
        self.db_name = db_name
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def create_db(self):
        """Создать новую базу данных"""
        conn = psycopg2.connect(host=self.host,
                                port=self.port,
                                user=self.user,
                                password=self.password)
        cursor = conn.cursor()
        conn.autocommit = True
        try:
            cursor.execute(f"CREATE DATABASE {self.db_name}")
            print(f'База данных "{self.db_name}" успешно создана')
        except psycopg2.errors.DuplicateDatabase:
            print(f'База данных "{self.db_name}" уже существует')
        finally:
            cursor.close()
            conn.close()

    def create_table(self, file):
        table = FileManager(Path(TABLES, file))
        print(table.load_file())

    def drop_table(self, table_name):
        pass

    def truncate_table(self, table_name):
        pass
