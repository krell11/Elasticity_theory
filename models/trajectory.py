import math
from models.material_body import MaterialBody
from utils.runge_kutta import runge_kutta


class Trajectory:
    def __init__(self, t: ()):
        self.time = t
        self.points = []

    def create_trajectory(self, body: MaterialBody):
        body_points = body.add_points_to_body(3)
        trajectories = []
        for point_num, target_point in enumerate(body_points):
            point_cords = (target_point.x, target_point.y)
            trajectories.append(runge_kutta(time_limits=self.time, points0=point_cords, h=0.01))
        self.points = trajectories
        return trajectories
