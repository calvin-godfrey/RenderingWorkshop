class Camera:
    def __init__(self, loc, to, up, aspect_ratio, vfov):
        """Parameters:
        location     -- Vector3
        direction    -- Vector3 target of camera
        up           -- 'up' direction relative to the camera.
        aspect_ratio -- width / height of plane
        vfov         -- vertical field of view, in degrees"""
        # implementation not included

    def generate_ray(self, x, y):
        """Takes an (x, y) pair (in [0, 1]), returns
        ray that starts at the camera that goes
        through that point on the plane."""
        # implementation not included