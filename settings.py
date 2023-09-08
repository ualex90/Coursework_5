import os
from pathlib import Path


# Дирректории
ROOT = Path(__file__).resolve().parent

FIXTURES = Path(ROOT, 'src', 'fixtures')
if not Path(FIXTURES).exists():
    FIXTURES.mkdir(parents=True)
