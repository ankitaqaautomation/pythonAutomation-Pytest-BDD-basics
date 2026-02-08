# this is a simple example of Inheritance in Python
# Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class).

class Car:           # Car is the parent class or Base class
    def __init__(self, brand, model, year, color="Black"):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
    
    def start_engine(self):
        return f"The engine of the {self.year} {self.brand} {self.model} is starting."
    
    def stop_engine(self):
        return f"The engine of the {self.year} {self.brand} {self.model} is stopping."
    
    def get_info(self):
        return f"{self.year} {self.brand} {self.model}"
    

class ElectricCar(Car):     # ElectricCar inherits from Car, child class
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year)    # Initialize attributes from the parent class i.e call parent constructor, Car
        self.battery_capacity = battery_capacity

    def start_engine(self):
        return f"The electric engine of the {self.year} {self.brand} {self.model} is starting silently."
    
    def charge_battery(self):
        return f"The battery of the {self.year} {self.brand} {self.model} is charging."
    

class GasolineCar(Car):   # Another child class inheriting from Car

    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)  # Call parent constructor, Car
        self.fuel_type = "Gasoline"

    def refuel(self):
        return f"The gasoline tank of the {self.year} {self.brand} {self.model} is being refueled."
    
    def start_engine(self):
        return f"The gasoline engine of the {self.year} {self.brand} {self.model} is starting with a roar."

# Example usage:
my_car = Car("Toyota", "Corolla", 2020)
print(my_car.get_info())  # Inherited method
print(my_car.start_engine())  # Inherited method
print(my_car.stop_engine())  # Inherited method

my_car.color = "Red"  # Accessing and modifying an attribute
print(f"My car color is: {my_car.color}")

gasoline_car = GasolineCar("Honda", "Civic", 2019)
print(gasoline_car.get_info())  # Inherited method
print(gasoline_car.refuel())  # New method in GasolineCar class


BMW = GasolineCar("BMW", "3 Series", 2021)
print(BMW.start_engine())  # Overridden method
print(gasoline_car.color)  # Accessing the color attribute of gasoline_car


tesla = ElectricCar("Tesla", "Model S", 2022, "100 kWh")   
print(tesla.get_info())  # Inherited method
print(tesla.start_engine())  # Overridden method
print(tesla.charge_battery())  # New method in ElectricCar class



# Accessing parent class method using super(), super can be used to access parent class methods
print(tesla.stop_engine())  # Inherited method from Car class
print(gasoline_car.stop_engine())  # Inherited method from Car class
print(BMW.stop_engine())  # Inherited method from Car class
print(BMW.get_info())  # Inherited method from Car class
print(BMW.refuel())  # New method in GasolineCar class
print(tesla.charge_battery())  # New method in ElectricCar class


# isinstance() and issubclass()
print(isinstance(tesla, ElectricCar))  # True
print(isinstance(tesla, Car))          # True
print(issubclass(ElectricCar, Car))    # True
print(issubclass(GasolineCar, Car))    # True
print(issubclass(Car, ElectricCar))     # False
print(issubclass(Car, GasolineCar))   # False


# Dunder methods are special methods in Python that start and end with double underscores (__). 
# They are also known as magic methods. 
# they allow you to define how objects of a class behave with

# Example: built-in operations and functions like __str__, _init__, _add__, _len__, etc.
# __init__ → runs when you create an object
# __del__ → runs when an object is deleted
# __str__ → controls what print(obj) shows
# __repr__ → official string representation of an object
# __len__ → lets your object work with len()
# __add__ → defines behavior for +
# __eq__ → defines ==


# Dunder variables
#Some dunders aren’t methods — they’re special variables:

# __name__ → module name (or "__main__")
# __file__ → file path of the module
# __dict__ → object’s attributes