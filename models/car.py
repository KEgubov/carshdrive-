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