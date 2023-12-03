from models.material_body import MaterialBody
from models.trajectory import Trajectory
from models.trajectory import function_a, function_b


def create_body(time, num_points,  **body_items):

    velocity = Trajectory(time)
    a_val = list(map(function_a, velocity.time))
    b_val = list(map(function_b, velocity.time))

    traj_points = [a_val, b_val]

    body = MaterialBody()

    for item, value in body_items.items():
        setattr(body, item, value)

    body_points = body.add_points_to_body(num_points)
    return body, body_points, traj_points
