import math


class MaterialPoint:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def get_radius_vector_length(self):
        return math.sqrt(self.x**2 + self.y**2)
