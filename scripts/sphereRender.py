# ...
white = Vector3(1, 1, 1)
blue = Vector3(0.5, 0.7, 1)
for y in range(height):
    for x in range(width):
        ray = camera.generate_ray(x / width, y / height)
        center = Vector3(0, 10, 0)
        radius = 5
        if sphere_intersection(center, radius, ray):
            color = Vector3(1, 0, 0) # red
        else: # background color
            t = (ray.direction.normalize().z + 1) / 2
            color = t * blue + (1 - t) * white
        wrapper.write_pixel(x, y, color)
wrapper.save()