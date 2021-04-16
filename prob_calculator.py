import copy
import random
# Consider using the modules imported above.

class Hat:
    """
    Performs many experiments to estimate an approximate probability.

    The approximate probability of drawing certain balls randomly from a hat
    can be simulated using a program as implemented here.

    Attributes:
        **kwargs (obj): `key=value` pairs that specify the number of balls of
        each color that are in the hat.
    """
    def __init__(self, **kwargs):
        """
        Initializes the Hat class with a list of balls of each color.

        Stores the arguments as a list of strings. Each string represents
        a single ball of that color.
        """
        self.contents = [k for k, v in kwargs.items() for i in range(v)]

    def draw(self, balls):
        """
        Removes balls at random from self.contents.
        
        Argument:
            balls (int): The number of balls to draw from the hat.

        Return:
           list: A list of balls randomly drawn from the hat as strings.
        """
        if balls > len(self.contents):
            return self.contents

        balls_drawn = random.sample(self.contents, k=balls)

        for ball in balls_drawn:
            self.contents.remove(ball)

        return balls_drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """
    Performs an experiment of drawing balls from a hat.

    Arguments:
        hat (obj): A Hat class object.
        expected_balls (obj): A group of balls to attempt to draw from the hat.
        num_balls_drawn (int): The number of balls to draw from the hat.
        num_experiments (int): The number of experiments to perform.

    Returns:
        float: The probability of drawing the balls from the hat.
    """
    successes = 0
    expected_balls = [k for k, v in expected_balls.items() for i in range(v)]

    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls_drawn = hat_copy.draw(num_balls_drawn)
        balls = []

        for ball in expected_balls:
            if ball in balls_drawn:
                balls_drawn.remove(ball)
                balls.append(ball)
    
        if sorted(expected_balls) == sorted(balls):
            successes += 1

    return successes / num_experiments
