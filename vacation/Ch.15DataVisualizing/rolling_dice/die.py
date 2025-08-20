from random import randint

class Die:
    """express a dice"""

    def __init__(self, num_sides=6):
        """6sides dice"""
        self.num_sides = num_sides

    def roll(self):
        """return random number from 1 to 6"""
        return randint(1, self.num_sides)