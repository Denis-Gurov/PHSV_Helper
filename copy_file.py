import shutil
import os

class FileCopier:
    def __init__(self, source_path=None, destination_path=None):
        self.source_path = source_path
        self.destination_path = destination_path

    def set_paths(self, source_path, destination_path):
        """Устанавливает пути для копирования файла."""
        self.source_path = source_path
        self.destination_path = destination_path

    def copy_file(self):
        """Копирует файл с заданного сетевого пути в локальную папку."""
        if not self.source_path or not self.destination_path:
            print("Ошибка: пути не заданы.")
            return

        try:
            shutil.copy(self.source_path, self.destination_path)
            print("Файл успешно скопирован!")
        except Exception as e:
            print(f"Ошибка при копировании файла: {e}")

    def delete_file(self, path):
        """Удаляет файл по указанному пути."""
        if not path:
            print("Ошибка: путь не задан.")
            return

        try:
            os.remove(path)
            print(f"Файл {path} успешно удален.")
        except FileNotFoundError:
            print(f"Ошибка: файл {path} не найден.")
        except Exception as e:
            print(f"Ошибка при удалении файла: {e}")