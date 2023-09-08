import json
from json import JSONDecodeError
from pathlib import Path

import yaml

from settings import FIXTURES


class FileManager:
    """
    Универсальный файловый менеджер.
    Способен работать с файлами формата json и yaml.
    Тип файла определяется расширением файла получив его название при инициализации.
    Работать с файлом возможно передав при инициализации объект Path либо указав название файла.
    Для сохранения файлов передавая только его название,
    необходимо заранее определить путь к дирректории по умолчанию - default_dir

    Доступны следующие методы:
    load_file() - Чтение файла. Если файл не существует, вернется None
    save_file(data) - Сохранить данные в файл. Если файл не существует, он будет создан
    update_file(new_data) - Обновление файла yaml или json
    """
    default_dir = FIXTURES

    def __init__(self, file_name) -> None:
        """Инициализация"""
        if isinstance(file_name, str):
            self.__file = Path(self.default_dir, file_name)
        elif isinstance(file_name, Path):
            self.__file = file_name
        self.__type = self._selection_type(file_name)

    @property
    def file(self):
        return self.__file

    @property
    def type(self):
        return self.__type

    @staticmethod
    def _selection_type(file_name) -> str:
        """Определение типа файла по имени"""
        if str(file_name).endswith('.json'):
            return 'json'
        elif str(file_name).endswith('.yaml'):
            return 'yaml'
        else:
            raise TypeError('Unknown file type. Change file type when initializing FileManager')

    def load_file(self):
        """Чтение из файла"""
        match self.__type:
            case 'json':
                return self._json_load()
            case 'yaml':
                return self._yaml_load()

    def save_file(self, data) -> bool:
        """
        Сохранение в файл
        :param data: Исходные данные
        """
        match self.__type:
            case 'json':
                self._json_save(data)
            case 'yaml':
                self._yaml_save(data)
        return True

    def update_file(self, new_data) -> bool:
        """
        Обновление файла.
        :param new_data: Новые данные типа dict либо list
        """
        data = None
        if self.__type == 'json':
            data = self._json_load()
        elif self.__type == 'yaml':
            data = self._yaml_load()
        if type(data) == type(new_data):
            if isinstance(data, dict) and isinstance(new_data, dict):
                data = dict() if data is None else data
                data.update(new_data)
            elif isinstance(data, list) and isinstance(new_data, list):
                data = list() if data is None else data
                data.extend(new_data)
        elif data is None:
            data = new_data
        else:
            raise TypeError("The data type in the file and new_data do not match. Check the new_data type.")
        if self.__type == 'json':
            self._json_save(data)
        elif self.__type == 'yaml':
            self._yaml_save(data)
        return True

    def _json_load(self):
        """Чтение файла .json"""
        try:
            with open(self.__file, 'r', encoding='UTF-8') as json_file:
                data = json.load(json_file)
        except JSONDecodeError:
            return None
        except FileNotFoundError:
            return None
        return data

    def _json_save(self, data, mode='w') -> None:
        """
        Сохранение данных в файл .json. Если файла не существует, он будет создан.
        :param data: Исходные данные типа dict или list
        :param mode: режим переписывания файла "w", дописывания "a"
        """
        if isinstance(data, dict) or isinstance(data, list):
            if not Path(self.__file).exists():
                mode = 'a'
            with open(self.__file, mode, encoding='UTF-8') as json_file:
                json.dump(data, json_file, ensure_ascii=False, indent=4)
        else:
            raise TypeError('The data must be of type "dict" or "list". Check data to save.')

    def _yaml_load(self):
        """Чтение файла .yaml"""
        try:
            with open(self.__file, "r", encoding="UTF-8") as yaml_file:
                data = yaml.safe_load(yaml_file)
        except FileNotFoundError:
            return None
        return data

    def _yaml_save(self, data, mode='w') -> None:
        """
        Сохранение данных в файл .yaml. Если файла не существует, он будет создан.
        :param data: Исходные данные типа dict или list
        :param mode: режим переписывания файла "w", дописывания "a"
        """
        if isinstance(data, dict) or isinstance(data, list):
            if not Path(self.__file).exists():
                mode = 'a'
            with open(self.__file, mode, encoding="UTF-8") as yaml_file:
                yaml.safe_dump(data, yaml_file, sort_keys=False, allow_unicode=True)
        else:
            raise TypeError('The data must be of type "dict" or "list". Check data to save.')

    def __repr__(self):
        return f'Path: {self.__file}\nType: {self.__type.upper()}'
