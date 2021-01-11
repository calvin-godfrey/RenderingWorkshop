# ...
samples = 50
for y in range(height):
    for x in range(width):
        final_color = Vector3(0, 0, 0)
        for _ in range(samples):
            ray = camera.generate_ray(x / width, y / height)
            color = get_intersection(ray, spheres, 20)
            final_color += color
        final_color /= samples
        wrapper.write_pixel(x, y, final_color)
    wrapper.save() # save more often