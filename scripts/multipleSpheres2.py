# takes ray, list of spheres; returns color
def get_intersection(ray, spheres):
    nearest = 1e100 # big number
    found_record = None
    for sphere in spheres:
        record = sphere.intersection(ray)
        if record is None:
            continue
        if record.time < nearest:
            found_record = record
            nearest = record.time
    if found_record == None:
        # This does simple gradient from earlier
        return get_background(ray)
    return found_record.color