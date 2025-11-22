'''QUESTION - Rotate a list K times
Given a list of items and an integer k, rotate the list to the right by k steps.

Consider that the list contains at least one item.

Example

>>> rotate_list([1, 2, 3, 4, 5], 2)
[4, 5, 1, 2, 3]
'''
#PLATFORM - IITM course

def rotate_list(lst: list, k: int) -> list:
    if not list:
        return lst
        
    n = len(lst)
    k = k % n
    
    if k == 0:
        return list
        
    return lst[-k:] + lst[:-k]