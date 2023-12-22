from utils.create_body import create_body
from utils.trajectory_plotter import trajectory_plotter
from models.trajectory import Trajectory
from models.stream_line import StreamLine
from models.space import Space
from models.space_point import SpacePoint
from utils.stream_line_plotter import plot_tangents
from utils.plot_velocity_field import plot_combined_graph
import numpy as np


time = (0.1, 1)
t = np.arange(time[0], time[1], 0.1)
ring = create_body(r1=1, r2=2, bounding_cond=(0, 90), num_points=200)
trajectory = Trajectory(time)

points = trajectory.create_trajectory(ring)
space_points_list = [SpacePoint(-5, -5), SpacePoint(10, 10)]
space = Space(space_points_list)
space.get_bounding_conditions()
space_bounding_x = space.x
space_bounding_y = space.y
trajectory_plotter(points, space_bounding_x, space_bounding_y)
stream_line = StreamLine(trajectory)
stream_line.calculate_tangents()
plot_tangents(stream_line, times=t)

#for t_ in t[::100]:
#   print(t_)
#    plot_combined_graph(stream_line, t_, x_range=space_bounding_x, y_range=space_bounding_y)