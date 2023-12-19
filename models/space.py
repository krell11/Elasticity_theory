from models.space_point import SpacePoint


class Space:
    def __init__(self, points: [SpacePoint]):
        self.points = points
        self.x = []
        self.y = []

    def get_bounding_conditions(self):
        x, y = [], []
        for point in self.points:
            x.append(point.x)
            y.append(point.y)

        self.x[0] = min(x)
        self.x[1] = max(x)
        self.y[0] = min(y)
        self.y[1] = max(y)
