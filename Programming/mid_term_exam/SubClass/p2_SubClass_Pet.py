import requests

#Get file
file = "http://jonghyup.com/tmp/objlab.py"
contents = requests.get(file).text
#print(contents)

#file contents
class Pet:
    def __init__(self):
        self.name = "NoName"
        self.age = 0

    def set_name(self, n):
        self.name = n

    def set_age(self, a):
        self.age = a

    def status(self):
        print("Name : %s" % self.name)
        print("Age  : %d" % self.age)

    def sound(self):
        pass

class Dog(Pet):
    """This class expresses a dog"""
    def run(self):
        print("Run Run Run")

    def sound(self):
        """Override sound()"""
        print("bark!")

class Cat(Pet):
    def jump(self):
        print("Jump Jump Jump")

    def sound(self):
        """Override sound()"""
        print("mew!")

class PersianCat(Cat):
    def set_name(self, n):
        self.name = "Persian" + str(n)
        print(self.name)


d = Dog()
d.set_name("Ben")
d.set_age(3)
d.status()
d.sound()
d.run()
print("_"*100)
c = Cat()
c.set_name("Aslan")
c.set_age(2)
c.status()
c.sound()
c.jump()
print("_"*100)
p = PersianCat()
p.set_name("Simba")
p.set_age(10)
p.status()
p.jump()


