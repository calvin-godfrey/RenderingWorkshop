def main():
    # Define constants, ImageWrapper, and Camera
    aspect_ratio = 1
    height = 256
    width = int(height * aspect_ratio) # force to be integer
    name = "test.png"
    wrapper = ImageWrapper(name, width, height)
    # Camera pointing from origin to (0, 1, 0) with z as up
    camera = Camera(Vector3(0, 0, 0), Vector3(0, 1, 0),
                    Vector3(0, 0, 1), aspect_ratio, 90)
    # ...
    #
    #
    #
    #
    #