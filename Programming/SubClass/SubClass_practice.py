#Animals
class Animal:
    """This class defines animal's name & species"""
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("The animal make a sound.")

    def info(self):
        print(f"Name: {self.name}, Species: {self.species}")


class Dog(Animal):
    """This sub_class expresses a dog"""
    def make_sound(self):
        print("woof, bow-wow, ruff!")

    def fetch(self):
        print(f"The {self.name} brings a ball!")

class Cat(Animal):
    """This sub_class expresses a cat"""
    def make_sound(self):
        print("meow, meow!")

    def climb(self):
        print(f"The {self.name} climbs a tree!")


dog = Dog("바둑이", "개")
cat = Cat("나비", "고양이")

dog.info()       # 이름: 바둑이, 종: 개
dog.make_sound() # 멍멍!
dog.fetch()      # 강아지가 공을 가져옵니다!

cat.info()       # 이름: 나비, 종: 고양이
cat.make_sound() # 야옹~
cat.climb()      # 고양이가 나무를 탑니다!


