class Car:
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance

    def __init__(self, brand=None, model=None, year=None):
        self.set_brand(brand)
        self.set_model(model)
        self.set_year(year)

    def set_brand(self, brand):
        if isinstance(brand, str) and len(brand) <= 20:
            self.brand = brand
        else:
            print("Error: Brand must be a string with maximum 20 characters.")

    def get_brand(self):
        return self.brand

    def set_model(self, model):
        if isinstance(model, str) and len(model) <= 20:
            self.model = model
        else:
            print("Error: Model must be a string with maximum 20 characters.")

    def get_model(self):
        return self.model

    def set_year(self, year):
        if isinstance(year, int) and 1900 <= year <= 2024:
            self.year = year
        else:
            print("Error: Year must be an integer between 1900 and 2024.")

    def get_year(self):
        return self.year


# Example usage:
car = Car()
car.set_brand("Toyota")
car.set_model("Camry")
car.set_year(2020)
print(car.get_brand())  # Output: Toyota
print(car.get_model())  # Output: Camry
print(car.get_year())   # Output: 2020
car.set_year(2025)      # Output: Error: Year must be an integer between 1900 and 2024.
car.set_brand("ThisIsAVeryLongBrandNameThatExceedsTwentyCharacters") # Output: Error: Brand must be a string with maximum 20 characters.
car.set_model("ThisIsAVeryLongModelNameThatExceedsTwentyCharacters") # Output: Error: Model must be a string with maximum 20 characters.