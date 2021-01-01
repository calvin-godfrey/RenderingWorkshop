# ...
white = Vector3(1, 1, 1)
blue = Vector3(0.5, 0.7, 1)
for y in range(height):
    for x in range(width):
        ray = camera.generate_ray(x / width, y / height)
        # map z in [-1, 1] to [0, 1]
        t = (ray.direction.normalize().z + 1) / 2
        # Linearly interpolate between white and blue
        color = t * blue + (1 - t) * white
        wrapper.write_pixel(x, y, color)
wrapper.save()