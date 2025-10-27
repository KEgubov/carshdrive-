from pyfiglet import Figlet

f = Figlet(font="slant")

ascii_art = f.renderText("CarshDrive")

print(ascii_art)


###########################Начало программы###################################
print('Добро пожаловать в "CarshDrive", пожалуйста, пройдите регистрацию!')

name = input("\nКак вас зовут? - ")

########################Безопасный ввод возраста##############################


def age_verification():

    while True:
        try:
            age = int(input("\nУкажите ваш возраст? - ").strip())
            break
        except ValueError:
            print("Пожалуйста, введите число (например, 21).")

    if age < 18:
        print(
            "\nВнимание! Регистрация на нашем сервисе доступна только "
            "после исполнения совершеннолетнего возраста."
        )

        raise SystemExit  # выходим, чтобы дальше код не выполнялся


age_verification()


#######################Более логичная регистрация##############################


def registration():

    while True:

        login = input("\nПридумайте логин: ").strip().lower()
        if len(login) < 8:
            print("\nЛогин должен содержать не менее 8 символов.")
        else:
            print("\nУспешно!")
            break

    while True:
        password = input("\nПридумайте пароль: ").strip().lower()
        if len(password) < 8:
            print("Пароль должен содержать не менее 8 символов.")
        else:
            print("\nУспешно!")
            break

    print(f"\nДобро пожаловать, {name.title()}! Регистрация успешно пройдена!")
    print("\nМашины, доступные для аренды: ")


registration()

######################### Создаём класс машин ###################################
class Car:
    def __init__(self, name, model, year, power, price: int, available: int):
        self.name = name
        self.model = model
        self.year = year
        self.power = power
        self.price = price
        self.available = available
        self.odometer_reading = 0

    def show_info_car(self):
        print(
            f"\nИмя: {self.name} \nМодель: {self.model} \nГод выпуска: {self.year} "
            f"\nМощность: {self.power} \nЦена: {self.price} "
            f"\nКоличество доступных машин: {self.available}"
        )

    def read_odometer(self):
        print(f"Пробег: {self.odometer_reading} км.")

    def update_odometer(self, mileage):
        self.odometer_reading = mileage


class ElectricCar(Car):

    def __init__(self, name, model, year, power, price: int, available: int):
        super().__init__(name, model, year, power, price, available)


######################### Создаём автопарк ###################################

cars = {
    "bmw": Car(
        "BMW",
        "BMW 3 Series",
        "2018",
        "2.0-литровый турбированный двигатель (255 л.с.)",
        5000,
        2,
    ),
    "mercedes": Car(
        "Mercedes",
        "Mercedes-AMG CLE 53",
        "2024",
        "3.0-литровый рядный 6-цилиндровый бензиновый двигатель (449 л.с.)",
        10000,
        3,
    ),
    "toyota": Car(
        "Toyota",
        "Toyota C-HR+ (EV)",
        "2025",
        "Электро, на платформе e-TNGA (343 л.с.)",
        8500,
        1,
    ),
    "tesla": ElectricCar(
        "Tesla", "Model 3", "2017", "Long Range RWD Electro AT (225.0 кВт)", 8000, 1
    ),
}
######################### Вспомогательные функции #############################


def show_info_cars(cars_dict):
    for car in cars_dict.values():
        car.show_info_car()


######################### Логика аренды #####################################


def rent_cars(cars_dict):

    show_info_cars(cars_dict)

    while True:

        user_data = (
            input(
                "\nКакую машину вы хотите взять на прокат? (Введите "
                "'quit', чтобы выйти.) "
            )
            .strip()
            .lower()
        )

        if user_data == "quit":
            exit("До скорой встречи! :)")

        if user_data in cars:
            car = cars[user_data]

            if car.available > 0:
                print(f"\nОтличный выбор! Ваша {car.model} ожидает вас в нашем центре!")
                # уменьшаем доступное количество
                car.available -= 1

                while True:

                    try:
                        days = int(
                            input(
                                "\nНа сколько дней берёте? (0 — пропустить расчёт): "
                            ).strip()
                        )
                        if days < 0:
                            print("Количество дней не может быть отрицательным.")
                            continue
                        if days > 0:
                            total = car.price * days
                            print(f"Итоговая стоимость за {days} дн.: {total} руб.")
                        break
                    except ValueError:
                        print("Введите целое число (например, 3).")
                break

            else:
                print("К сожалению, эта модель закончилась.")
                user_data = (
                    input("Попробуйте выбрать другую машину (bmw/mercedes/toyota): ")
                    .strip()
                    .lower()
                )
                return user_data

        else:
            print(
                "К сожалению, такой машины у нас ещё нет, но мы обязательно "
                "учтём ваши предпочтения!"
            )

            user_data = input("Попробуйте выбрать другую машину: ").lower()
            return user_data


rent_cars(cars)


################################Оценка сервиса#################################
def get_service_grade():
    # Функция запрашивает у пользователя оценку сервиса от 1 до 5.
    #     Если пользователь вводит 'quit', программа завершает работу.

    while True:

        user_input = input(
            '\nПожалуйста, поставьте оценку нашему сервису "CarshDrive"'
            ", где 1 - плохо, 5 - хорошо: (Введите 'quit', чтобы выйти) "
        )

        if user_input.lower() == "quit":
            print("\nДо скорой встречи! :)")
            return None

        try:

            grade = int(user_input)

            if grade in [1, 2]:
                print("\nМне очень жаль, что мы не оправдали ваших ожиданий :(")
                return grade

            elif grade in [3, 4, 5]:
                print("\nБлагодарю за отзыв! Ваше мнение помогает нам стать лучше.")
                return grade

            else:
                print("Пожалуйста, введите оценку от 1 до 5.")

        except ValueError:
            print("Пожалуйста, введите число (например, 5).")


user_grade = get_service_grade()

if user_grade is not None:
    print("\nВаша оценка:", user_grade)
else:
    print("Вы вышли без оценки.")

########################Возможность арендовать ещё машины #####################


def rent_car_two():
    while True:

        user = input(
            '\nЖелаете ли вы арендовать ещё какую нибудь машину? "Да" или "Нет" (Введите "quit", чтобы выйти). - '
        )

        if user.lower() == "quit":
            exit("До скорой встречи! :)")

        elif user.lower() in ["да", "yes"]:
            show_info_cars(cars)
            rent_cars(cars)

        elif user.lower() in ["нет", "no"]:
            exit("До скорой встречи! :)")

        else:
            print('\nПожалуйста, введите "Да" или "Нет".')


rent_car_two()
