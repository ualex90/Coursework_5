import psycopg2


class DB:
    """Базовый класс для работы с базой данных"""
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
