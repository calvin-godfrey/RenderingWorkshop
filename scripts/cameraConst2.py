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
	    # define the height/width of plane
        # ...
        #
        #
        #
        #