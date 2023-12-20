import matplotlib.pyplot as plt
from models.stream_line import StreamLine
import os

images_folder = "images_path/"
image_name = "streamline.png"


def plot_tangents(stream: StreamLine, scale=1):
    plt.figure()
    for trajectory, tangents in zip(stream.trajectory.points, stream.tangents):
        x_vals, y_vals = zip(*trajectory)
        plt.plot(x_vals, y_vals, label='Trajectory')

        for point, tangent in zip(trajectory[::5], tangents):
            start_point = (point[0] - scale * tangent[0], point[1] - scale * tangent[1])
            end_point = (point[0] + scale * tangent[0], point[1] + scale * tangent[1])
            plt.plot([start_point[0], end_point[0]], [start_point[1], end_point[1]], 'r-')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.savefig(os.path.join(images_folder + image_name))
    plt.show()
