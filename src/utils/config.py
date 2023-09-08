from pathlib import Path

from settings import CONFIG
from src.utils.file_manager import FileManager


class Config:
    def __init__(self) -> None:
        self.employers = dict()
        self.employers_file = FileManager(Path(CONFIG, 'employers.yaml'))

    def add_employers(self, data: dict) -> None:
        self.employers_file.update_file(data)

    def get_employers(self) -> dict:
        data = self.employers_file.load_file()
        if data is None:
            return dict()
        return data
