from models.material_body import MaterialBody


def create_body(**body_items):
    body = MaterialBody()

    for item, value in body_items.items():
        setattr(body, item, value)
    return body
