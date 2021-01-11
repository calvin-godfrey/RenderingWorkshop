# takes ray, list of spheres; returns color
def get_intersection(ray, spheres):
    nearest = 1e100 # big number
    found_record = None
    for sphere in spheres:
        record = sphere.intersection(ray)
        if record is None:
            continue
    # ...
    #
    #
    #
    #
    #
    #