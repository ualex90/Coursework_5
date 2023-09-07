import json
from json import JSONDecodeError
from pathlib import Path

import yaml

from settings import FIXTURES


class FileManager:
    def __init__(self, file_name: str) -> None:
        self.file = Path(FIXTURES, file_name)
        self.type = self._selection_type(file_name)

    @staticmethod
    def _selection_type(file_name: str) -> str:
        """Определение типа файла по имени"""
        if file_name.endswith('.json'):
            return 'json'
        elif file_name.endswith('.yaml'):
            return 'yaml'
        else:
            raise TypeError('Unknown file type. Change file type when initializing FileManager')

    def load_file(self):
        """Чтение из файла"""
        match self.type:
            case 'json':
                return self._json_load()
            case 'yaml':
                return self._yaml_load()

    def save_file(self, data) -> None:
        """
        Сохранение в файл
        :param data: Исходные данные
        """
        match self.type:
            case 'json':
                self._json_save(data)
            case 'yaml':
                self._yaml_save(data)

    def update_file(self, new_data: dict) -> None:
        """
        Обновление файла. Актуально только для файлов содержащие словари не обернутые в список
        :param new_data: Новые данные типа dict
        """
        data = None
        if self.type == 'json':
            data = self._json_load()
        elif self.type == 'yaml':
            data = self._yaml_load()
        if isinstance(data, dict) or data is None:
            data = dict() if data is None else data
            data.update(new_data)
            if self.type == 'json':
                self._json_save(data)
            elif self.type == 'yaml':
                data = self._yaml_load()

    def _json_load(self):
        """Чтение файла .json"""
        try:
            with open(self.file, 'r', encoding='UTF-8') as json_file:
                data = json.load(json_file)
        except JSONDecodeError:
            return None
        except FileNotFoundError:
            return None
        return data

    def _json_save(self, data, mode='w') -> None:
        """
        Сохранение данных в файл .json. Если файла не существует, он будет создан.
        :param data: Исходные данные
        :param mode: Режим переписывания файла "w", дописывания "a"
        """
        if not Path(self.file).exists():
            mode = 'a'
        with open(self.file, mode, encoding='UTF-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)

    def _yaml_load(self):
        """Чтение файла .yaml"""
        try:
            with open(self.file, "r", encoding="UTF-8") as yaml_file:
                data = yaml.safe_load(yaml_file)
        except FileNotFoundError:
            pass
        return data

    def _yaml_save(self, data, mode='w') -> None:
        """
        Сохранение данных в файл .yaml. Если файла не существует, он будет создан.
        :param data: Исходные данные
        :param mode: режим переписывания файла "w", дописывания "a"
        """
        if not Path(self.file).exists():
            mode = 'a'
        with open(self.file, mode, encoding="UTF-8") as yaml_file:
            yaml.safe_dump(data, yaml_file, sort_keys=False, allow_unicode=True)


if __name__ == '__main__':
    f = FileManager('jik.yaml')
    f.save_file({'hjk': 8})
    print(f.load_file())
