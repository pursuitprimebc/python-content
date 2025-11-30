'''QUESTION - Check if right triangle with even side lengths
Given three side lengths in the increasing order of length as a, b, and c, where a<=b<=c, check if the given sides are the sides of a right triangle whose perpendicular sides are of even length.
'''
#PLATFORM - IITM Course

def is_right_triangle_with_even_sides(a:int,b:int,c:int) -> bool:
    is_right_triangle = (a * a + b * b == c * c)
    both_perpendicular_even = (a% 2 ==0) and (b%2==0)
    return is_right_triangle and both_perpendicular_even
