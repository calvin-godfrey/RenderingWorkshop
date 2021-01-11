class Sphere:
    def __init__(self, center, radius, color):
        self.center = center
        self.radius = radius
        self.color = color

    def intersection(self, ray):
        diff = ray.origin - self.center
        a = ray.direction.dot(ray.direction)
        b = diff.dot(2 * ray.direction)
        c = diff.dot(diff) - self.radius * self.radius
        solutions = solve_quadratic(a, b, c)
        for solution in solutions:
            if solution > 0:
                return (True, self.color)
        return (False, self.color)