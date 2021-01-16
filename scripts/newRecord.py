class HitRecord:
    def __init__(self, point, material, time, normal):
        self.point = point
        self.normal = normal
        self.time = time
        self.material = material