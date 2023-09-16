import psycopg2
from pathlib import Path

from settings import TABLES
from src.utils.file_manager import FileManager


class DBCreator:
    """Создание базы данных"""

    def __init__(self, db_name: str = None, user: str = None,
                 password: str = None, host='localhost', port='5432') -> None:
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

    def connection(self) -> psycopg2.connect:
        try:
            conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                dbname=self.db_name,
                user=self.user,
                password=self.password,
                connect_timeout=2)
        except psycopg2.OperationalError as description:
            message = self.operational_error_message(description)
            print(message)
            print('-' * len(message))
        else:
            return conn

    def create_db(self) -> bool:
        """Создать новую базу данных"""
        is_create = False
        try:
            conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password)
        except psycopg2.OperationalError as description:
            message = self.operational_error_message(description)
            print(message)
            print('-' * len(message))
            return is_create
        cursor = conn.cursor()
        conn.autocommit = True
        try:
            cursor.execute(f"CREATE DATABASE {self.db_name}")
            message = f'Создана база данных "{self.db_name}"'
            print(message)
            print('-' * len(message))
            is_create = True
        except psycopg2.errors.DuplicateDatabase:
            message = f'База данных "{self.db_name}" уже существует'
            print(message)
            print('-' * len(message))
            is_create = True
        finally:
            cursor.close()
            conn.close()
        return is_create

    def operational_error_message(self, description: psycopg2.OperationalError) -> str:
        """Формирование сообщения при возникновении ошибки подключения"""
        message = "Ошибка соединения"
        if f'could not translate host name "{self.host}" to address' in str(description):
            message = f'Не удалось перевести имя хоста "{self.host}" в адрес'
        if 'failed: timeout expired' in str(description):
            message = f'Ошибка соединения с "{self.host}:{self.port}". Превышено время ответа'
        if f'Connection refused' in str(description):
            message = (f'Сервер "{self.host}:{self.port}" не найден. '
                       f'Проверьте работоспособность сервера на этом хосте')
        if 'FATAL:  password authentication failed for user' in str(description):
            message = f'подключение к "{self.host}:{self.port}" прервано. Неверный пароль'
        if f'database "{self.db_name}" does not exist' in str(description):
            message = f'База данных "{self.db_name}" на сервере "{self.host}:{self.port}" не существует'
        return message

    def create_table(self, file):
        """Создать новую таблицу"""
        table = FileManager(Path(TABLES, file)).load_file()
        create_table_instruction = self.get_create_table_instruction(table)
        conn = self.connection()
        if conn:
            try:
                with conn:
                    with conn.cursor() as cursor:
                        try:
                            cursor.execute(create_table_instruction)
                            message = f'Создана таблица "{table.get("name")}" из файла "{file}"'
                            print(message)
                            print('-' * len(message))
                        except psycopg2.errors.DuplicateTable:
                            message = f'Таблица "{table.get("name")}" уже существует'
                            print(message)
                            print('-' * len(message))
            finally:
                conn.close()

    @staticmethod
    def get_create_table_instruction(table) -> str:
        """Формирование инструкции для создания новой таблицы"""
        table_name = table.get('name')
        columns = list()
        constraints = list()
        for column in table.get('columns'):
            # Создание полей колонок
            columns.append(
                f'{column.get("name")} '
                f'{column.get("data_type")}'
                f'{" NOT NULL" if column.get("is_not_null") else ""}')
            # Создание полей ограничений
            if column.get('constraints'):
                match column['constraints']['type']:
                    case 'primary_key':
                        constraints.append(
                            f'CONSTRAINT {column["constraints"]["name"]} '
                            f'PRIMARY KEY({column["name"]})')
                    case 'foreign_key':
                        constraints.append(
                            f'CONSTRAINT {column["constraints"]["name"]} '
                            f'FOREIGN KEY({column["name"]}) '
                            f'REFERENCES {column["constraints"]["parent_table"]}'
                            f'({column["constraints"]["parent_key_columns"]})')
                    case 'check':
                        constraints.append(
                            f'CONSTRAINT {column["constraints"]["name"]} '
                            f'CHECK({column["constraints"]["check"]})')
                    case 'unique':
                        pass
                    case 'exclude':
                        pass
        # Формирование строки инструкции
        create_table_instruction = (f'CREATE TABLE {table_name} '
                                    f'({", ".join(columns)}'
                                    f'{(", " + ", ".join(constraints)) if constraints else ""})')
        return create_table_instruction

    def truncate_table(self, table_name):
        """Очистить таблицу"""
        conn = self.connection()
        if conn:
            try:
                with conn:
                    with conn.cursor() as cursor:
                        try:
                            cursor.execute(f'TRUNCATE TABLE {table_name} RESTART IDENTITY CASCADE')
                            message = f'Удалены данные из таблицы "{table_name}"'
                            print(message)
                            print('-' * len(message))
                        except psycopg2.errors.UndefinedTable:
                            message = f'Таблица "{table_name}" не существует'
                            print(message)
                            print('-' * len(message))
            finally:
                conn.close()

    def drop_table(self, table_name):
        """Удалить таблицу"""
        conn = self.connection()
        if conn:
            try:
                with conn:
                    with conn.cursor() as cursor:
                        try:
                            cursor.execute(f'DROP TABLE {table_name}')
                            message = f'Удалена таблица "{table_name}"'
                            print(message)
                            print('-' * len(message))
                        except psycopg2.errors.UndefinedTable:
                            message = f'Таблица "{table_name}" не существует'
                            print(message)
                            print('-' * len(message))
            finally:
                conn.close()

    def fill_table(self, data):
        """Заполнить таблицу"""
        conn = self.connection()
        if conn:
            try:
                with conn:
                    for tables in data:
                        for table, lines in tables.items():
                            with conn.cursor() as cursor:
                                records_list_template = ', '.join(['%s'] * len(lines[0]))
                                try:
                                    cursor.executemany(
                                        f'INSERT INTO {table} '  # Проработать вопрос по использыванию execute с целью отлавливания дубликатов
                                        f'VALUES ({records_list_template})',
                                        map(lambda x: tuple(x.values()), lines))
                                except psycopg2.errors.UniqueViolation:
                                    pass
                                except psycopg2.errors.InFailedSqlTransaction:
                                    message = f'Неизвестная ошибка. Текущая транзакция прерывается'
                                    print(message)
                                    print('-' * len(message))

                    message = f'Данные успешно добавлены в базу'
                    print(message)
                    print('-' * len(message))
            finally:
                conn.close()
