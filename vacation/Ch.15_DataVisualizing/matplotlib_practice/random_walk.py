from random import choice



class RandomWalk:
    """make RandomWalk"""

    def __init__(self, num_points=5000):
        """settings initialization"""
        self.num_points = num_points

        #inital coordinate
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """assign the direction & distance"""
        direction = choice([-1, 1])
        distance = choice(range(0, 10, 1))
        return distance * direction

    def fill_walk(self):
        """calculate each of RandomWalk's points"""

        while len(self.x_values) < self.num_points:
            #assign x,y location
            x_step = self.get_step()
            y_step = self.get_step()

            # calculate new location
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

            # revoke the location data when its movements is '0'
            if x_step == 0 and y_step == 0:
                continue


