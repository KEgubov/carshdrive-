print('Добро пожаловать в "CarshDrive", пожалуйста, пройдите регистрацию!')

name = input("\nКак вас зовут? - ")

# Безопасный ввод возраста
while True:
    try:
        age = int(input("Укажите ваш возраст? - ").strip())
        break
    except ValueError:
        print("Пожалуйста, введите число (например, 21).")

login = input("Придумайте логин: ").strip().lower()
password = input("Придумайте пароль: ").strip().lower()

if age < 18:
    print(
        "Внимание! Регистрация на нашем сервисе доступна только "
        "после исполнения совершеннолетнего возраста."
    )

    raise SystemExit  # выходим, чтобы дальше код не выполнялся

print(f"\nДобро пожаловать, {name.title()}! Регистрация успешно пройдена!")
print("\nМашины, доступные для аренды: ")

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

# Вывод списка машин для аренды
for car, details in cars.items():
    full_details = (
        f'\nМарка машины: {car.title()} \nМодель: {details["model"]} '
        f'{details["year"]} \nХарактеристики: {details["power"]}'
    )
    print(full_details)
    print(f'Цена: {details["price"]} руб.')
    print(f'Количество машин доступных для аренды: {details["available"]}.')

# ----- Выбор машины -----
user_data = input("\nКакую машину вы хотите взять на прокат? ").strip().lower()

while True:  # Заказ машины

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

    else:
        print(
            "К сожалению, такой машины у нас ещё нет, но мы обязательно "
            "учтём ваши предпочтения!"
        )

        user_data = input("Попробуйте выбрать другую машину: ").lower()

# ----- Оценка сервиса -----
while True:

    grade = int(
        input(
            '\nПожалуйста, поставьте оценку нашему сервису "CarshDrive"'
            ", где 1 - плохо, 5 - хорошо: "
        )
    )

    try:

        if grade in [1, 2]:
            print("\nМне очень жаль, что мы не оправдали ваших ожиданий :(")
            break

        elif grade in [3, 4, 5]:
            print("\nБлагодарю за отзыв! Ваше мнение помогает нам стать лучше.")
            break

        else:
            print("Пожалуйста, введите оценку от 1 до 5.")

    except ValueError:
        print("Пожалуйста, введите число (например, 5).")
