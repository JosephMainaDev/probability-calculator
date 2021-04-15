import copy
import random
# Consider using the modules imported above.

class Hat:
    """
    Perform a large number of experiments to estimate an approximate probability.

    Arguments:
        key=value pairs that specify the number of balls of each color
        that are in the hat.
    """
    def __init__(self, **kwargs):
        """
        Store the arguments as a list of strings.
        Each string represents a single ball of that color.
        """
        self.contents = [k for k, v in kwargs.items() for i in range(v)]

    def draw(self, balls):
        """
        Removes balls at random from self.contents.
        
        Argument:
            balls: represents the number of balls to draw from the hat.

        Return:
            A list of balls as strings.
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
        hat: A hat object.
        expected_balls: A group of balls to attempt to draw from the hat.
        num_balls_drawn: The number of balls to draw from the hat in each experiment.
        num_experiments: The number of experiments to perform.

    Returns:
        A probability as a float.
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
