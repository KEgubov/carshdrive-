# ===================== Импорты =====================

from pyfiglet import Figlet
from models.registration import Registration
from models.car import cars

# ===================== Заголовок =====================
f = Figlet(font="slant")

ascii_art = f.renderText("CarshDrive")

print(ascii_art)


###########################Начало программы###################################
print('Добро пожаловать в "CarshDrive", пожалуйста, пройдите регистрацию!')


###########################Регистрация пользователя###########################
registration = Registration("", 0, "", "")
registration.user_name()
registration.age_verification()
registration.set_login()
registration.set_password()

######################### Вспомогательные функции #############################


def show_info_cars(cars_dict):
    for car in cars_dict.values():
        car.show_info_car()


######################### Логика аренды #####################################


def rent_cars(cars_dict):
    while True:
        show_info_cars(cars_dict)

        user_data = (
            input(
                "\nКакую машину вы хотите взять на прокат? (Введите "
                "'quit', чтобы выйти.) "
            )
            .strip()
            .lower()
        )

        if user_data == "quit":
            print("До скорой встречи! :)")
            return None

        if user_data not in cars_dict:
            print(
                "К сожалению, такой машины у нас ещё нет, но мы обязательно учтём ваши предпочтения!"
            )
            continue

        car = cars_dict[user_data]

        if car.available <= 0:
            print("\nК сожалению, эта модель закончилась.")
            print("\nВыберите другую модель из списка.")
            continue

        print(f'\nОтличный выбор! Ваша {car.model} ожидает вас в нашем центре!')
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


        while True:
            again = input(
                '\nХотите арендовать ещё одну машину? (да/нет) ').strip().lower()
            if again in ("да", "yes", "y"):
                # цикл внешней функции повторится
                break
            elif again in ("нет", "no", "n"):
                print("\nСпасибо! Возвращаемся в главное меню.")
                return None
            else:
                print('\nПожалуйста, введите "да" или "нет".')

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
            rent_cars(cars)

        elif user.lower() in ["нет", "no"]:
            exit("До скорой встречи! :)")

        else:
            print('\nПожалуйста, введите "Да" или "Нет".')


rent_car_two()
