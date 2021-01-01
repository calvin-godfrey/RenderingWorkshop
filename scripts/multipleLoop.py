# ...
# same constants as before
spheres = [Sphere(Vector3(0, 10, 0), 5, Vector3(1, 0, 0)),
    Sphere(Vector3(0, 10, -100), 95, Vector3(0.2, 1, 0.1))]
for y in range(height):
    for x in range(width):
        ray = camera.generate_ray(x / width, y / height)
        color = get_intersection(ray, spheres)
        wrapper.write_pixel(x, y, color)
wrapper.save()