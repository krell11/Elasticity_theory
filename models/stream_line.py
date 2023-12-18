from models.trajectory import Trajectory
import matplotlib.pyplot as plt


class StreamLine:
    def __init__(self, trajectory: Trajectory):
        self.trajectory = trajectory
        self.tangents = []

    def calculate_tangents(self):
        self.tangents = []
        for trajectory in self.trajectory.points:
            tangents_for_trajectory = []
            for i in range(0, len(trajectory) - 1, 5):
                dx = trajectory[i + 1][0] - trajectory[i][0]
                dy = trajectory[i + 1][1] - trajectory[i][1]
                tangents_for_trajectory.append((dx, dy))
            self.tangents.append(tangents_for_trajectory)

    def plot_tangents(self, scale=1):
        plt.figure()
        for trajectory, tangents in zip(self.trajectory.points, self.tangents):
            x_vals, y_vals = zip(*trajectory)
            plt.plot(x_vals, y_vals, label='Trajectory')

            for point, tangent in zip(trajectory[::5], tangents):
                start_point = (point[0] - scale * tangent[0], point[1] - scale * tangent[1])
                end_point = (point[0] + scale * tangent[0], point[1] + scale * tangent[1])
                plt.plot([start_point[0], end_point[0]], [start_point[1], end_point[1]], 'r-')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.show()
