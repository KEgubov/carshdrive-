# =========== Импорты ==========

from pyfiglet import Figlet
from carshdrive.services.registration import Registration
from carshdrive.models.car import cars
from carshdrive.services.rent_cars import rent_cars, rent_car_two
from carshdrive.services.service_grade import get_service_grade

# =========== Заголовок =========
f = Figlet(font="slant")

ascii_art = f.renderText("CarshDrive")

print(ascii_art)


# =========== Начало программы =============
def main():
    print('Добро пожаловать в "CarshDrive", пожалуйста, пройдите регистрацию!')
    # =========== Регистрация пользователя ============
    registration = Registration("", 0, "", "")
    registration.user_name()
    registration.age_verification()
    registration.set_login()
    registration.set_password()
    # =========== Вывод машин и логика аренды ============
    print("\nСписок машин доступных для аренды:")
    rent_cars(cars)
    # =========== Оценка сервиса ============
    user_grade = get_service_grade()

    if user_grade is not None:
        print("\nВаша оценка:", user_grade)
    else:
        print("Вы вышли без оценки.")
    # =========== Возможность арендовать ещё машины ============
    rent_car_two()
    return "ok"


if __name__ == "__main__":
    result = main()
