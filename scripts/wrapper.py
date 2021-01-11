class ImageWrapper:
    def __init__(self, name, width, height):
        # ...

    def save(self):
        # ...

    def write_pixel(self, x, y, color):
        # Assumes color is Vector3 and
        # 0 <= x < width, 0 <= y < height
        # ...