class Camera:
    # ...
    def generate_ray(self, x, y):
        # x, y both in [0, 1)
        # scale left/right and up/down vector by x, y
        point = self.lower_left \
              + x * self.x_vec \
              + y * self.y_vec
        # direction is vector from origin to point on plane
        direction = point - self.origin
        return Ray(self.origin, direction)