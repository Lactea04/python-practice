from car import Car


class IceCreamStand():
    def __init__(self):
        self.FLAVORS = ['Banana', 'Chocolate', 'Strawberry', 'Watermelon']

    def get_FLAVORS(self):
        print(f"There are {len(self.FLAVORS)} types flavors for Icecream."
              f"\n{self.FLAVORS}")

class Restaurant():
    def __init__(self, name, cuisine_type):
        """식당 이름과 다루는 요리 초기값 설정"""
        self.restaurant_name = str(name)
        self.cuisine_type = str(cuisine_type)
        self.FLAVORS = IceCreamStand()

    def describe_restaurant(self):
        """식당 이름과 다루는 요리 설명"""
        print(f"The restaurant's name is {self.restaurant_name}\n"
              f"and its cuisine type is {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"The restaurant is opened!")
#instanciation
chicken = Restaurant("BBQ", "chicken")
pizza = Restaurant("Domino", "pizza")
Icecream = Restaurant("Baskin_Robbins", "Icecream")

my_new_car = Car('audi','a4','2024')
print(my_new_car.get_describe_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()