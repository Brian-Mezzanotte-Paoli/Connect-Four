from random import randint

class IA:
    def __init__(self, matrix):
        self.matrix = matrix

    def get_choice(self):
        return randint(0,6)
