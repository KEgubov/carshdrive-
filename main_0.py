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


cars = {
    "bmw": {
        "model": "BMW 3 Series",
        "year": 2018,
        "power": "2.0-литровый турбированный двигатель (255 л.с.)",
        "price": 5000,
        "available": 2,
    },
    "mercedes": {
        "model": "Mercedes-AMG CLE 53",
        "year": 2024,
        "power": "3.0-литровый рядный 6-цилиндровый бензиновый двигатель (449 л.с.)",
        "price": 10000,
        "available": 3,
    },
    "toyota": {
        "model": "Toyota C-HR+ (EV)",
        "year": 2025,
        "power": "Электро, на платформе e-TNGA (343 л.с.)",
        "price": 8500,
        "available": 1,
    },
}


#############################Вывод списка машин для аренды####################
def show_info_cars(cars):
    for car, details in cars.items():
        full_details = (
            f'\nМарка машины: {car.title()} \nМодель: {details["model"]} '
            f'{details["year"]} \nХарактеристики: {details["power"]}'
            f'\nЦена: {details["price"]} руб'
            f'\nКоличество машин доступных для аренды: {details["available"]}.'
        )
        print(full_details)


show_info_cars(cars)


############################Заказ Машины######################################
def rent_cars():
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
            if cars[user_data]["available"] > 0:
                print(
                    f'\nОтличный выбор! Ваша {cars[user_data]["model"]} ожидает вас в нашем центре!'
                )
                # уменьшаем доступное количество
                cars[user_data]["available"] -= 1

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
                            total = cars[user_data]["price"] * days
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


rent_cars()


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
            rent_cars()

        elif user.lower() in ["нет", "no"]:
            exit("До скорой встречи! :)")

        else:
            print('\nПожалуйста, введите "Да" или "Нет".')


rent_car_two()