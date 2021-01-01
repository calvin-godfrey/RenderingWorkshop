def rand_on_sphere():
    # random.random() returns [0, 1),
    # map to the range [-1, 1]
    v = Vector3(2 * random.random() - 1,
                2 * random.random() - 1,
                2 * random.random() - 1)
    return v.normalize() # make unit vector