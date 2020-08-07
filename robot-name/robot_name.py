import random
import string


class Robot:
    def __init__(self):
        self.name = self.generate_robot_name()

    def reset(self):
        while self.generate_robot_name() == self.name:
            self.name = self.generate_robot_name()

    def generate_robot_name(self):
        alphabets = random.choices(string.ascii_uppercase, k=2)
        letters = "".join(alphabets)
        numbers = random.choices(string.digits, k=3)
        digits = "".join(numbers)

        return str(letters+digits)
