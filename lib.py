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
        # print(color)
        r = max(min(int(color[0] * 255), 255), 0) # Clamps in [0, 1)
        g = max(min(int(color[1] * 255), 255), 0) # Clamps in [0, 1)
        b = max(min(int(color[2] * 255), 255), 0) # Clamps in [0, 1)
        # print(f"{r}, {g}, {b}")
        self.pixels[x, y] = (r, g, b)