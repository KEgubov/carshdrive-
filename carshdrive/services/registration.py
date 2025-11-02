class Registration:
    def __init__(self, name, age, login, password):
        self.name = name
        self.age = age
        self.login = login
        self.password = password

    def user_name(self):

        while True:

            self.name = input("\nКак вас зовут? - ").strip().lower()

            if any(char.isdigit() for char in self.name):
                print('\nОшибка: Имя не может состоять из цифр!')
                continue

            if not self.name:
                print('\nОшибка: Имя не может быть пустым!')
                continue

            return self.name

    def age_verification(self):

        while True:
            try:
                self.age = int(input("\nУкажите ваш возраст? - ").strip())
                break
            except ValueError:
                print("Пожалуйста, введите число (например, 21).")

        if self.age < 18:
            print(
                "\nВнимание! Регистрация на нашем сервисе доступна только "
                "после исполнения совершеннолетнего возраста."
            )

            raise SystemExit  # выходим, чтобы дальше код не выполнялся

    def set_login(self):

        while True:

            self.login = input("\nПридумайте логин: ").strip().lower()
            if len(self.login) < 8:
                print("\nЛогин должен содержать не менее 8 символов.")
            else:
                print("\nУспешно!")
                break

    def set_password(self):

        while True:
            self.password = input("\nПридумайте пароль: ").strip().lower()
            if len(self.password) < 8:
                print("Пароль должен содержать не менее 8 символов.")
            else:
                print("\nУспешно!")
                break

        print(f"\nДобро пожаловать, {self.name.title()}! Регистрация успешно пройдена!")

