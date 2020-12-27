from lib import Vector3, Ray, ImageWrapper
import math

class Camera:
    def __init__(self, location, to, up, aspect_ratio, vfov):
        """Camera constructor. Parameters:

        location -- Vector3

        direction -- Vector3, location camera is pointed at.
        up -- direction that points 'up' relative to the camera.
        These three parameters are used to form an orthogonal basis
        that is then used to generate rays.
        """
        w = (to - location).normalize() # vector pointing to target from camera location
        u = w.cross(up).normalize() # points in the left/right direction
        v = u.cross(w).normalize() # points in the up/down direction
        # Now w, u, v are all orthogonal vectors
        self.origin = location
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

def sphere_intersection(center, radius, ray):
    diff = ray.origin - center
    a = ray.direction.dot(ray.direction)
    b = diff.dot(2 * ray.direction)
    c = diff.dot(diff) - radius * radius
    solutions = solve_quadratic(a, b, c)
    # Because solutions are in increasing order,
    # we can iterate until we find a positive one
    for solution in solutions:
        if solution > 0:
            return True
    return False

def main():
    aspect_ratio = 1
    width = 256
    height = int(width / aspect_ratio) # round
    name = "test.png"
    wrapper = ImageWrapper(name, width, height)
    camera = Camera(Vector3(0, 0, 0), Vector3(0, 1, 0), Vector3(0, 0, 1), 1, 90)
    white = Vector3(1, 1, 1)
    blue = Vector3(0.5, 0.7, 1)
    for y in range(height):
        for x in range(width):
            ray = camera.generate_ray(x / width, y / height)
            sphere_center = Vector3(0, 10, 0)
            sphere_radius = 5
            if sphere_intersection(sphere_center, sphere_radius, ray):
                color = Vector3(1, 0, 0) # red
            else:
                t = (ray.direction.z + 1) / 2
                # background sky color
                color = t * white + (1 - t) * blue
            wrapper.write_pixel(x, y, color)

    wrapper.save()

if __name__ == '__main__':
    main()