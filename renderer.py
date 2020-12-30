from lib import Vector3, Ray, ImageWrapper
import math, random

MAX_DEPTH = 20

class Camera:
    def __init__(self, loc, to, up, aspect_ratio, vfov):
        """Camera constructor. Parameters:

        location -- Vector3

        direction -- Vector3, location camera is pointed at.
        up -- direction that points 'up' relative to the camera.
        These three parameters are used to form an orthogonal basis
        that is then used to generate rays.
        """
        w = (to - loc).normalize() # vector pointing to target from camera location
        u = w.cross(up).normalize() # points in the left/right direction
        v = w.cross(u).normalize() # points in the up/down direction
        # Now w, u, v are all orthogonal vectors
        self.origin = loc
        focal_length = 1 # Arbitrary constant
        plane_height = 2 * math.tan(vfov * math.pi / 360)
        plane_width = plane_height * aspect_ratio
        self.x_vec = u * plane_width
        self.y_vec = v * plane_height
        self.lower_left = self.origin - self.x_vec / 2 - self.y_vec / 2 + w * focal_length



    def generate_ray(self, x, y):
        """This function takes an (x, y) pair (both in [0, 1)) and returns a
        ray that starts at the camera and goes through that point on the camera's
        projection plane.
        """
        direction = self.lower_left + x * self.x_vec + y * self.y_vec - self.origin
        return Ray(self.origin, direction)

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
    def __init__(self, point, normal, color, time):
        self.point = point
        self.normal = normal # used later
        self.color = color
        self.time = time

class Sphere:
    def __init__(self, center, radius, color):
        self.center = center
        self.radius = radius
        self.color = color

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
                return HitRecord(p, normal, self.color, solution)
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
    direction = found_record.normal + rand_on_sphere()
    new_ray = Ray(found_record.point, direction)
    return found_record.color.multiply(get_intersection(new_ray, spheres, depth - 1))

def main():
    aspect_ratio = 1
    height = 256
    width = int(height * aspect_ratio) # round
    name = "test.png"
    wrapper = ImageWrapper(name, width, height)
    camera = Camera(Vector3(0, 0, 0), Vector3(0, 1, 0), Vector3(0, 0, 1), 1, 90)
    spheres = [Sphere(Vector3(0, 10, 0), 5, Vector3(1, 0, 0)),
               Sphere(Vector3(0, 10, -100), 95, Vector3(0.2, 1, 0.1))]
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