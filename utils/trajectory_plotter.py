from models.material_body import MaterialBody
from models.material_point import MaterialPoint
from models import trajectory
import matplotlib.pyplot as plt
import numpy as np
import os


images_folder = "images_path/"


def trajectory_plotter(points_coordinates: []):

    plt.figure(figsize=(10, 10))
    for point_num, point in enumerate(points_coordinates):
        x_vals = [cord[0] for cord in point]
        y_vals = [cord[1] for cord in point]
        plt.plot(x_vals, y_vals)

    plt.grid(True)
    plt.show()
