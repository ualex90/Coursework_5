import shutil
from pathlib import Path

import pytest

from src.utils.file_manager import FileManager


# Создание и очистка перед новым тестом директории test_fixtures
test_root = Path(__file__).resolve().parent
test_fixtures = Path(test_root, 'test_fixtures')
if Path(test_fixtures).exists():
    shutil.rmtree(test_fixtures)
test_fixtures.mkdir(parents=True)


@pytest.fixture
def json_file_dict():
    return FileManager(Path(test_fixtures, 'dict.json'))


@pytest.fixture
def json_file_list():
    return FileManager(Path(test_fixtures, 'list.json'))


@pytest.fixture
def yaml_file_dict():
    return FileManager(Path(test_fixtures, 'dict.yaml'))


@pytest.fixture
def yaml_file_list():
    return FileManager(Path(test_fixtures, 'list.yaml'))


@pytest.fixture
def json_file_none():
    return FileManager(Path(test_fixtures, 'none.json'))


@pytest.fixture
def yaml_file_none():
    return FileManager(Path(test_fixtures, 'none.yaml'))


@pytest.fixture
def json_file_bad():
    file_path = Path(test_fixtures, 'bad.json')
    file = FileManager(Path(test_fixtures, 'bad.json'))
    with open(file_path, 'a', encoding='UTF-8') as f:
        f.write('qwerty')
    return file
