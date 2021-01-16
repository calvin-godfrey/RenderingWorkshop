class Sphere:
    # ...
    def intersection(self, ray):
        diff = ray.origin - self.center
        a = ray.direction.dot(ray.direction)
        b = diff.dot(2 * ray.direction)
        c = diff.dot(diff) - self.radius * self.radius
        solutions = solve_quadratic(a, b, c)
        for solution in solutions:
            if solution > 0: # new code to make HitRecord
                p = ray.at(solution)
                return HitRecord(p, self.color, solution)
        return None