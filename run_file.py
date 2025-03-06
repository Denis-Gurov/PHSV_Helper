import os

class ExeRunner:
    def __init__(self, exe_path=None):
        self.exe_path = exe_path

    def set_exe_path(self, exe_path):
        """Устанавливает путь к .exe файлу."""
        self.exe_path = exe_path

    def run(self):
        """Запускает .exe файл, если путь задан."""
        if not self.exe_path:
            print("Ошибка: путь к .exe файлу не задан.")
            return

        try:
            exit_code = os.system(f'"{self.exe_path}"')
            if exit_code == 0:
                print("Программа успешно запущена.")
            else:
                print(f"Произошла ошибка, код завершения: {exit_code}")
        except Exception as e:
            print(f"Произошла ошибка при запуске программы: {e}")