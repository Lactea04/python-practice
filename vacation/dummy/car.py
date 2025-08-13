class Car:
    """자동타 클래스"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_describe_name(self):
        """브랜드, 모델, 제조연도"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """주행계 읽기"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """주행계 수정"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increase_odometer(self, miles):
        """주행계 늘리기"""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """supply some fuel"""
        print("The gas tank is filled completely!!")


class Battery:
    """This class describes the electric car's battery"""

    def __init__(self, battery_size = 40):
        """배터리 초기값 초기화"""
        self.battery_size = battery_size

    def describe_battery(self):
        """배터리 크기 설명"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """This method describe when the car is on a full charge, how this car can go by this battery"""
        if self.battery_size == 40:
            range_ = 150
        elif self.battery_size == 65:
            range_ = 225
        print(f"This car can go about {range_} miles on a full charge")

    def upgrade_battery(self):
        if self.battery_size < 65:
            self.battery_size = 65


class ElectricCar(Car):
    """전기차에만 있는 특징 정의"""

    def __init__(self, make, model, year):
        """부모 클래스의 속성 초기화"""
        super().__init__(make, model, year)
        self.battery = Battery()


    def fill_gas_tank(self): #method override
        """전기차에는 연료통이 없음"""
        print("Thers is no gas tank in electric car.")