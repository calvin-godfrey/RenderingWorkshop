def sphere_intersection(center, radius, ray):
    diff = ray.origin - center # O - C
    a = ray.direction.dot(ray.direction) # D . D
    b = diff.dot(2 * ray.direction) # 2D . (O - C)
    c = diff.dot(diff) - radius * radius
    solutions = solve_quadratic(a, b, c)
    # Because solutions are in increasing order,
    # we can iterate until we find a positive solution
    for solution in solutions:
        if solution > 0:
            return True
    return False