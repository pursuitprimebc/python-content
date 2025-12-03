'''QUESTION - Reverse First half in an even length tuple
Given an even-length tuple t, return a new tuple where the first half of the tuple is reversed, and the second half remains unchanged.

Example

t = (1, 2, 3, 4, 5, 6)
The first half (1, 2, 3) is reversed to (3, 2, 1), so the result is (3, 2, 1, 4, 5, 6).
'''
# PLATFORM - IITM course

def reverse_first_half(t: tuple) -> tuple:
    
    mid_point = len(t) // 2
    first_half = t[:mid_point]
    second_half = t[mid_point:]
    
    return first_half[::-1] + second_half
    


