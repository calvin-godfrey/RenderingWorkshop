# generate new ray direction
direction = found_record.material.scatter(found_record, ray)
new_ray = Ray(found_record.point, direction)
curr_color = found_record.material.color
next_color = get_intersection(new_ray, sphere, depth - 1)
return curr_color.multiply(next_color)