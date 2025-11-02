from carshdrive.models.car import cars
########################Вывод списка машин ####################################
def show_info_cars(cars_dict):
    for car in cars_dict.values():
        car.show_info_car()
#########################Логика аренды машин##################################
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