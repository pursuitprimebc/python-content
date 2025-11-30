''' QUESTION - Find Manhattan distance between two 2d points through a point
Given three points a, b, and c on the Cartesian plane, calculate the Manhattan distance to go from point a to point c via point b.

Manhattan distance is the sum of the absolute differences of their Cartesian coordinates.
'''
# PLATFORM -  IITM course

def manhattan_distance_via_b(a: tuple, b: tuple, c: tuple) -> int:
    distance_a_to_b = abs(a[0] - b[0]) + abs(a[1] - b[1])
    distance_b_to_c = abs(b[0] - c[0]) + abs(b[1] - c[1])
    return distance_a_to_b + distance_b_to_c