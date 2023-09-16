from pathlib import Path

from settings import CONFIG
from src.utils.file_manager import FileManager


class Config:
    def __init__(self) -> None:
        self.employers = dict()
        self.employers = FileManager(Path(CONFIG, 'employers.yaml'))
        self.server = FileManager(Path(CONFIG, 'server.yaml'))

    def add_employers(self, data: dict) -> None:
        self.employers.update_file(data)

    def get_employers(self) -> dict:
        data = self.employers.load_file()
        if data is None:
            return dict()
        return data

    def add_server(self, data: dict):
        self.server.save_file(data)

    def get_server(self) -> dict:
        data = self.employers.load_file()
        if data is None:
            return dict()
        return data
