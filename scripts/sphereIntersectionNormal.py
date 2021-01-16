# ...
# rest is the same
for solution in solutions:
    if solution > 0: # new code to make HitRecord
        p = ray.at(solution)
        normal = (p - self.center).normalize()
        # add normal as parameter to HitRecord
        return HitRecord(p, self.color, solution, normal)