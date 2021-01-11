class Camera:
    def __init__(self, loc, to, up, aspect_ratio, vfov):
        self.origin = loc
        w = (to - loc).normalize() # points to target from camera
        u = w.cross(up).normalize() # points in left/right of plane
        v = w.cross(u).normalize() # points in the up/down direction
        # w, u, v are all orthogonal vectors
        focal_length = 1 # Arbitrary
        plane_height = 2 * math.tan((vfov * math.pi / 180) / 2)
        plane_width = plane_height * aspect_ratio
        self.x_vec = u * plane_width
        self.y_vec = v * plane_height
        self.lower_left = self.origin - self.x_vec / 2 \
                        - self.y_vec / 2 + w * focal_length
        # self.origin + w * focal_length is middle of plane,
        # subtraction gives location of bottom left corner