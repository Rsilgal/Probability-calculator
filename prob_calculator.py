import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)

    def __str__(self):
        res = ''

        for elem in self.contents:
            res += '{}\n'.format(elem)
        
        return res

    def draw(self, num_balls_drawn):
        result = []

        if (num_balls_drawn >= len(self.contents)):
            return self.contents

        for i in range(num_balls_drawn):
            rand = random.randrange(len(self.contents))
            result.append(self.contents[rand])
            self.contents.pop(rand)

        return result

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_desired_results = 0

    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)

        actual = hat_copy.draw(num_balls_drawn)
        
        # Convert result to dict:
        actual_dict = {ball: actual.count(ball) for ball in set(actual)}

        # Compare drawn balls to desired result:
        result = True
        for key, value in expected_balls.items():
            if key not in actual_dict or actual_dict[key] < expected_balls[key]:
                result = False
                break

        if result:
            num_desired_results += 1

    return num_desired_results/num_experiments