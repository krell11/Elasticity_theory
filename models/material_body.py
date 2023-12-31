from models.material_point import MaterialPoint
import numpy as np


class MaterialBody:
    def __init__(self, x: float = 0.1, y: float = 0.1,
                 r1: float = 0, r2: float = 0,
                 bounding_cond=(0, 0), num_points: int = 0):
        self.x = x
        self.y = y
        self.r1 = r1
        self.r2 = r2
        self.bounding_cond = bounding_cond
        self.body_points = []
        self.num_points = num_points

    def add_points_to_body(self) -> list[MaterialPoint]:
        points = []
        #while len(points) < self.num_points:
        #    x = np.random.rand()
        #    y = np.random.rand()
        #    distance = (x**2 + y**2) ** 0.5
        #    if self.r1 <= distance <= self.r2 and x >= 0 and y >= 0:
        #        points.append(MaterialPoint(x, y))

        for radius in [self.r1, self.r2]:
            for angle in np.linspace(0, np.pi/2 , self.num_points):
                x = 5 + radius * np.cos(angle)
                y = 5 + radius * np.sin(angle)
                if x > 0 and y > 0:
                    points.append(MaterialPoint(x, y))

        return points
