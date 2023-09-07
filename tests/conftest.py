from pathlib import Path

import pytest

from src.utils.file_manager import FileManager

test_root = Path(__file__).resolve().parent
test_fixtures = Path(test_root, 'fixtures')
if not Path(test_fixtures).exists():
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
