import os
from pathlib import Path


# Корневая директория
ROOT = Path(__file__).resolve().parent

# Директория по умолчанию для сохранения данных
DATA = Path(ROOT, 'src', 'fixtures')
if not Path(DATA).exists():
    DATA.mkdir(parents=True)

# Директория для хранения файлов конфигурации
CONFIG = Path(ROOT, 'config')
if not Path(CONFIG).exists():
    CONFIG.mkdir(parents=True)
