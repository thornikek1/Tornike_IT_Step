class Car:
    number_of_cars = 0
    
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        Car.number_of_cars += 1
    
    def car_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")
    
    def age_of_car(self, current_year):
        return current_year - self.year
    
    @classmethod
    def total_cars(cls):
        print(f"Total number of cars: {cls.number_of_cars}")


class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_life):
        super().__init__(brand, model, year)
        self.battery_life = battery_life
    
    def battery_info(self):
        print(f"The battery life of this machine is {self.battery_life} hours")


# მაგალითი:
car1 = Car("Toyota", "Camry", 2018)
car2 = Car("Honda", "Accord", 2020)
car3 = ElectricCar("Tesla", "Model S", 2022, 400)

# ავტომობილებზე ინფორმაციის გამოტანა
car1.car_info()
car2.car_info()
car3.car_info()

# ასაკის გამოთვლა
current_year = 2024
print("Age of car:", car1.age_of_car(current_year))

# ბატარიის ინფორმაციის გამოტანა
car3.battery_info()

# ავტომობილების ჯამური რაოდენობა
Car.total_cars()
