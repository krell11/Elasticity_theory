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

        self.x.append(min(x))
        self.x.append(max(x))
        self.y.append(min(y))
        self.y.append(max(y))
        print(self.x)