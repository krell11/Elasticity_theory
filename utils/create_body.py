from models.material_body import MaterialBody
from models.trajectory import Trajectory
from utils.functions import function_a, function_b


def create_body(**body_items):
    body = MaterialBody()

    for item, value in body_items.items():
        setattr(body, item, value)
    return body
