from pathlib import Path


class FileManager:
    def __init__(self, file: Path) -> None:
        self.file = file
        self.type = None

    def load_file(self):
        pass

    def save_file(self):
        pass
