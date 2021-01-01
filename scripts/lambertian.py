class Lambertian:
    def __init__(self, color):
        # color is Vector3
        self.color = color

    def scatter(self, record, ray):
        # returns direction for next ray
        return record.normal + rand_on_sphere()