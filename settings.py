import os
from pathlib import Path

from dotenv import load_dotenv

# Переменные окружения
load_dotenv()
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')

# Основные директории
ROOT = Path(__file__).resolve().parent
SRC = Path(ROOT, 'src')

# Директория по умолчанию для сохранения данных
DATA = Path(SRC, 'fixtures')
if not Path(DATA).exists():
    DATA.mkdir(parents=True)

# Директория для хранения файлов конфигурации
CONFIG = Path(ROOT, 'config')
if not Path(CONFIG).exists():
    CONFIG.mkdir(parents=True)

# Директория для хранения файлов YAML с данными для создания таблиц
TABLES = Path(SRC, 'data_base', 'tables')
