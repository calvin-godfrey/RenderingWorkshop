red = Lambertian(Vector3(1, 0, 0))
green = Lambertian(Vector3(0.2, 1, 0.1))
spheres = [Sphere(Vector3(0, 10, 0), 5, red),
           Sphere(Vector3(0, 10, -100), 95, green)]
# same loop body as before