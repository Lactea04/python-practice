class Fruit:
    """This class expresses a fruit"""
    def __init__(self, color, type):
        self.color = color
        self.type = type

    def show(self):
        """Show fruit's type and color"""
        print(f"Type: {self.type}, Color : {self.color}")

s1 = Fruit('yellow', 'fig')
s2 = Fruit('red', 'apple')

s1.show()
s2.show()