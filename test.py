from utils.create_body import create_body
from utils.trajectory_plotter import trajectory_plotter
from models.trajectory import Trajectory
from models.stream_line import StreamLine
from models.space import Space
from models.space_point import SpacePoint
from utils.stream_line_plotter import plot_tangents

time = (0.1, 5)
ring = create_body(r1=1, r2=2, bounding_cond=(0, 90), num_points=20)
trajectory = Trajectory(time)

points = trajectory.create_trajectory(ring)

space_points_list = [SpacePoint(0, 7), SpacePoint(1, 0)]
space = Space(space_points_list)
space.get_bounding_conditions()
space_bounding_x = space.x
space_bounding_y = space.y
trajectory_plotter(points, space_bounding_x, space_bounding_y)
stream_line = StreamLine(trajectory)
stream_line.calculate_tangents()
plot_tangents(stream_line)
