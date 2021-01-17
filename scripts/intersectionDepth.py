def get_intersection(ray, spheres, depth):
    if depth == 0: # too many bounces
        return Vector3(0, 0, 0) # black
    found_record = None
    # same logic to find closest intersection as before
    # ...
    # generate new ray direction
    direction = found_record.normal + rand_on_sphere()
    new_ray = Ray(found_record.point, direction)
    # color of next bounce
    next_color = get_intersection(new_ray, spheres, depth - 1)
    current_color = found_record.color
    # This is compontent-wise multiplication
    return current_color.multiply(next_color)