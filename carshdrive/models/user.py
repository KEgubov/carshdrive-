import json
import os
from carshdrive.services.registration import Registration

class User(Registration):
    def __init__(self, name, age, login, password):
        super().__init__(name, age, login, password)

    def save_to_json(self, filename="user_data.json"):
        """Сохраняет данные пользователя в JSON-файл."""
        # Формируем данные текущего пользователя
        user_data = {
            "name": self.name,
            "age": self.age,
            "login": self.login,
            "password": self.password
        }

        try:
            # 1. Инициализируем пустой список для данных
            data = []

            # 2. Если файл существует — читаем его
            if os.path.exists(filename):
                with open(filename, "r", encoding="utf-8") as f:
                    try:
                        loaded = json.load(f)  # Пытаемся загрузить JSON
                        # Если загружено несколько пользователей (список)
                        if isinstance(loaded, list):
                            data = loaded
                        # Если загружен один пользователь (словарь)
                        elif isinstance(loaded, dict):
                            data = [loaded]
                        # Если другой тип — игнорируем и оставляем пустой список
                    except json.JSONDecodeError as e:
                        print(f"Ошибка декодирования JSON из {filename}: {e}")
                        # data остаётся пустым списком

            # 3. Добавляем нового пользователя в список
            data.append(user_data)

            # 4. Сохраняем весь список обратно в файл
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

        except (OSError, IOError) as e:
            print(f"Ошибка файловой системы при работе с {filename}: {e}")
        except Exception as e:
            print(f"Неожиданная ошибка: {e}")
