import math
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

    def create_table(self, columns: list, data: list):
        """Формирование и вывод в консоль табличных данных"""
        view_page = 0  # просматриваемая страница
        self.clear_screen()
        while True:
            results = len(data)              # Количество строк
            pages = math.ceil(results / 10)  # Количество страниц
            data_start = view_page * 10      # Индекс элемента для первой строки

            # Количество строк на одной странице
            range_list = 10 if view_page + 1 < pages or results == 10 else results % 10

            # Формирование заголовка
            title_list = [f'{i[0]:^{i[1]}}' for i in columns]
            title = f'|{"№":^7}| {"| ".join(title_list)} |'
            print(f'{title}\n|{"=" * (len(title) - 2)}|')

            # Формирование строк
            for n in range(range_list):
                item = data[data_start]
                string_list = list()
                for i, j in zip(item, columns):
                    if str(i).isdigit():
                        string_list.append(f'{i:^{j[1]}}')
                    else:
                        string_list.append(f'{(f"{i[:(j[1] - 4)]}..." if len(i) > j[1] else i):<{j[1]}}')
                print(f'|{data_start + 1:^7}| {"| ".join(string_list)} |')
                data_start += 1
            print(f'\nСтраница {view_page + 1} из {pages}')
            print('(q): в меню, (z): назад, (ENTER): вперед\n')

            # Навигация
            user_input = input('>> ').lower().strip()
            if user_input == 'q':
                self.clear_screen()
                return
            elif user_input == 'z':
                self.clear_screen()
                view_page -= 1 if view_page > 0 else view_page
            elif user_input == '':
                if pages > view_page + 1:
                    self.clear_screen()
                    view_page += 1
                else:
                    self.clear_screen()
            else:
                self.clear_screen()
                print('Попробуйте еще раз. Необходимо ввести букву навигации\n')
