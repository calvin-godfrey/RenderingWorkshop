from PIL import Image
import numpy as np
import math

class Vector3:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
    def __sub__(self, v):
        return Vector3(self.x-v.x,self.y-v.y,self.z-v.z)
    def __add__(self, v):
        return Vector3(self.x+v.x,self.y+v.y,self.z+v.z)
    def __mul__(self, s): # Multiplication by scalar
        return Vector3(self.x*s,self.y*s,self.z*s)
    def __truediv__(self, s):
        return Vector3(self.x/s,self.y/s,self.z/s)
    def multiply(self, v): # Component-wise
        return Vector3(self.x*v.x,self.y*v.y,self.z*v.z)
    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
    def normalize(self):
        return self / self.length()
    def cross(self, b):
        return Vector3(self.y*b.z - self.z*b.y, self.z*b.x - self.x*b.z, self.x*b.y - self.y*b.x)
    __rmul__ = __mul__
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    def __getitem__(self, key):
        return [self.x, self.y, self.z][key]

class Ray:
    def __init__(self, origin, direction):
        """Ray constructor. Parameters:

        origin -- Vector3
        direction -- Vector3 (which becomes normalized)
        tmin -- float
        """
        self.origin = origin
        self.direction = direction.normalize()
    def __str__(self):
        return f"{self.origin}: {self.direction}"

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
        self.horizontal_vec = u * plane_width
        self.vertical_vec = v * plane_height
        self.lower_left_corner = self.origin - self.horizontal_vec / 2 - self.vertical_vec / 2 + w * focal_length



    def generate_ray(self, x, y):
        """This function takes an (x, y) pair (both in [0, 1)) and returns a
        ray that starts at the camera and goes through that point on the camera's
        projection plane.
        """
        direction = self.lower_left_corner + x * self.horizontal_vec + y * self.vertical_vec - self.origin
        return Ray(self.origin, direction)

class ImageWrapper:
    def __init__(self, image, name):
        """
        Contains a Pillow Image and file name
        """
        self.image = image
        self.pixels = image.load()
        self.name = name

    def save(self):
        """
        Save current progress of image
        """
        self.image.save(self.name)

    def write_pixel(self, x, y, color):
        """
        Writes the given RGB triplet at the given pixel.
        Assumes that each color component is in [0, 1)
        """
        # print(color)
        r = max(min(int(color[0] * 255), 255), 0) # Clamps in [0, 1)
        g = max(min(int(color[1]  * 255), 255), 0) # Clamps in [0, 1)
        b = max(min(int(color[2] * 255), 255), 0) # Clamps in [0, 1)
        # print(f"{r}, {g}, {b}")
        self.pixels[x, y] = (r, g, b)


def main():
    height = 256
    width = 256
    name = "test.png"
    im = Image.new("RGB", (width, height))
    wrapper = ImageWrapper(im, name)
    camera = Camera(Vector3(0, 0, 0), Vector3(0, 1, 0), Vector3(0, 0, 1), 1, 60)
    for y in range(height):
        for x in range(width):
            ray = camera.generate_ray(x / width, y / height)
            t = 0.5 * ray.direction.z + 1
            color = t * Vector3(1, 1, 1) + (1 - t) * Vector3(0.5, 0.7, 1) # Linear interpolation
            wrapper.write_pixel(x, y, color)

        wrapper.save()

if __name__ == '__main__':
    main()