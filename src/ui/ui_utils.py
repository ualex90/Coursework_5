import os


class UIUtils:
    def __init__(self) -> None:
        self.operating_system = os.name  # Тип операционной системы

    def clear_screen(self) -> None:
        """
        Отправка команды на очистку экрана консоли
        в зависимости от операционной системы
        """
        if self.operating_system == 'nt':
            os.system('cls')
        else:
            os.system('clear')
