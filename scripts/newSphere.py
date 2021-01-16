class Sphere:
    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material # updated
    def intersection(self, ray):
        diff = ray.origin - self.center
        a = ray.direction.dot(ray.direction)
        b = diff.dot(2 * ray.direction)
        c = diff.dot(diff) - self.radius * self.radius
        solutions = solve_quadratic(a, b, c)
        for solution in solutions:
            if solution > 0:
                p = ray.at(solution)
                normal = (p - self.center).normalize()
                # Now we also have to update HitRecord
                return HitRecord(p, self.material, solution, normal)
        return None