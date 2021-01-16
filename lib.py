import math
from PIL import Image

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
    def dot(self, v):
        return self.x * v.x + self.y * v.y + self.z * v.z
    __rmul__ = __mul__
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    def __getitem__(self, key):
        return [self.x, self.y, self.z][key]

class Ray:
    def __init__(self, origin, direction):
        """Ray constructor. Parameters:

        origin -- Vector3
        direction -- Vector3
        """
        self.origin = origin
        self.direction = direction

    def at(self, t):
        return self.origin + t * self.direction

    def __str__(self):
        return f"{self.origin}: {self.direction}"

class ImageWrapper:
    def __init__(self, name, width, height):
        """
        Contains a Pillow Image and file name
        """
        self.image = Image.new("RGB", (width, height))
        self.pixels = self.image.load()
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
        gamma = 2.2
        r = max(min(color[0], 1), 0) # Clamps in [0, 1)
        g = max(min(color[1], 1), 0) # Clamps in [0, 1)
        b = max(min(color[2], 1), 0) # Clamps in [0, 1)
        r = int(round((r ** gamma) * 256))
        g = int(round((g ** gamma) * 256))
        b = int(round((b ** gamma) * 256))
        # print(f"{r}, {g}, {b}")
        self.pixels[x, y] = (r, g, b)

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