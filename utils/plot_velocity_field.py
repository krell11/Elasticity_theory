import numpy as np
from utils.runge_kutta import dif_sys_func
import matplotlib.pyplot as plt
from utils.stream_line_plotter import plot_tangents
from scipy.integrate import odeint


def plot_velocity_field(t, x_range, y_range, resolution=20):
    x, y = np.meshgrid(np.linspace(x_range[0], x_range[1], resolution),
                       np.linspace(y_range[0], y_range[1], resolution))
    u, v = np.zeros_like(x), np.zeros_like(y)
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            velocity = dif_sys_func(t, (x[i, j], y[i, j]))
            u[i, j], v[i, j] = velocity[0], velocity[1]
    plt.figure(figsize=(8, 6))
    plt.quiver(x, y, u, v, scale=5)
    plt.streamplot(x, y, u, v, density=1.5, color='b')
    plt.gca().set_aspect('equal', adjustable='box')


def plot_combined_graph(streamline, t, x_range, y_range):
    plt.figure(figsize=(10, 6))

    plot_velocity_field(t, x_range, y_range, resolution=20)
    plt.show()