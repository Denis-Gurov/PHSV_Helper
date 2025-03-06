import subprocess
import os


def clone_or_update_repo(repo_url, local_path):
    try:
        if not os.path.exists(local_path):
            print(f"Клонируем репозиторий из {repo_url} в {local_path}...")
            subprocess.run(['git', 'clone', repo_url, local_path], check=True)
            print("Репозиторий успешно клонирован.")
        else:
            print(f"Обновляем репозиторий в {local_path}...")
            os.chdir(local_path)
            subprocess.run(['git', 'pull'], check=True)
            print("Репозиторий успешно обновлен.")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при выполнении команды git: {e}")
    except Exception as ex:
        print(f"Произошла ошибка: {ex}")
