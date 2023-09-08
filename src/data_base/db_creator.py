import psycopg2


class DBCreator:
    """Создание базы данных"""

    def __init__(self, db_name: str, user: str, password: str,
                 default_dbname='postgres', host='localhost', port='5432') -> None:
        """
        Инициализация

        :param db_name: Имя базы данных с которой предстоит работать далее
        :param user: Имя пользователя
        :param password: Пароль
        :param default_dbname: Имя существующей базы данных (необходимо для первоначального подключения)
        :param host: Адрес сервера
        :param port: Порт сервера
        """
        self.db_name = db_name
        self.user = user
        self.password = password
        self.default_db_name = default_dbname
        self.host = host
        self.port = port

    def create_db(self):
        conn = psycopg2.connect(host=self.host,
                                port=self.port,
                                dbname=self.default_db_name,
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

    def create_table(self):
        pass

    def drop_table(self):
        pass

    def truncate_table(self):
        pass
