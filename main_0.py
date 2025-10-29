# ===================== Импорты =====================

from pyfiglet import Figlet
from services.registration import Registration
from models.car import cars
from services.rent_cars import rent_cars

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

##########################Вызов функции вывода машин###########################
######################### Логика аренды #######################################
print('\nСписок машин доступных для аренды:')
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
