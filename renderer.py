from lib import Vector3, Ray, ImageWrapper, Camera
import math, random

MAX_DEPTH = 20

def solve_quadratic(a, b, c):
    desc = b * b - 4 * a * c
    if desc < 0: # No real solution
        return []
    if desc == 0: # Single solution
        return [-b / (2 * a)]
    else:
        sqrt_desc = math.sqrt(desc)
        b_minus = (-b - sqrt_desc) / (2 * a)
        b_plus = (-b + sqrt_desc) / (2 * a)
        # Always return smaller solution first
        return [min(b_minus, b_plus), max(b_minus, b_plus)]

class HitRecord:
    def __init__(self, point, normal, time, material):
        self.point = point
        self.normal = normal
        self.time = time
        self.material = material

class Sphere:
    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def intersection(self, ray):
        diff = ray.origin - self.center
        a = ray.direction.dot(ray.direction)
        b = diff.dot(2 * ray.direction)
        c = diff.dot(diff) - self.radius * self.radius
        solutions = solve_quadratic(a, b, c)
        for solution in solutions:
            if solution > 0:
                p = ray.at(solution)
                normal = (p - self.center).normalize()
                return HitRecord(p, normal, solution, self.material)
        return None

def get_background(ray):
    direction = ray.direction.normalize()
    white = Vector3(1, 1, 1)
    blue = Vector3(0.5, 0.7, 1)
    t = (direction.z + 1) / 2
    return t * blue + (1 - t) * white

def rand_on_sphere():
    v = Vector3(2 * random.random() - 1,
                2 * random.random() - 1,
                2 * random.random() - 1)
    return v.normalize()
    

def get_intersection(ray, spheres, depth):
    if depth == 0:
        return Vector3(0, 0, 0) # black
    nearest = 1e100 # big number
    found_record = None
    for sphere in spheres:
        record = sphere.intersection(ray)
        if record is None:
            continue
        if record.time < nearest:
            found_record = record
            nearest = record.time
    if found_record == None:
        return get_background(ray)
    # generate new ray direction
    direction = found_record.material.scatter(found_record, ray)
    new_ray = Ray(found_record.point, direction)
    curr_color = found_record.material.color
    return curr_color.multiply(get_intersection(new_ray, spheres, depth - 1))
    
class Lambertian:
    def __init__(self, color):
        self.color = color

    def scatter(self, record, ray):
        # returns direction for next ray
        return record.normal + rand_on_sphere()

def main():
    aspect_ratio = 1
    height = 256
    width = int(height * aspect_ratio) # round
    name = "test.png"
    wrapper = ImageWrapper(name, width, height)
    red = Lambertian(Vector3(1, 0, 0))
    green = Lambertian(Vector3(0.2, 1, 0.1))
    camera = Camera(Vector3(0, 0, 0), Vector3(0, 1, 0), Vector3(0, 0, 1), 1, 90)
    spheres = [Sphere(Vector3(0, 10, 0), 5, red),
               Sphere(Vector3(0, 10, -100), 95, green)]
    samples = 50
    for y in range(height):
        for x in range(width):
            final_color = Vector3(0, 0, 0)
            for sample in range(samples):
                ray = camera.generate_ray((x + random.random()) / width, (y + random.random()) / height)
                color = get_intersection(ray, spheres, MAX_DEPTH)
                final_color += color
            final_color /= samples
            wrapper.write_pixel(x, y, final_color)
        wrapper.save()

if __name__ == '__main__':
    main()