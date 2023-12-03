import math


class Trajectory:
    def __init__(self, t: []):
        self.time = t


def function_a(x):
    return -(math.exp(x) - math.exp(-x)) // 2


def function_b(x):
    return math.sin(x)