samples = 50
for y in range(height):
    for x in range(width):
        final_color = Vector3(0, 0, 0)
        for sample in range(samples):
            ox = x + random.random() # offset x
            oy = y + random.random() # offset y
            ray = camera.generate_ray(ox / width, oy / height)
            color = get_intersection(ray, spheres, MAX_DEPTH)
            final_color += color
        final_color /= samples
        wrapper.write_pixel(x, y, final_color)
    wrapper.save()