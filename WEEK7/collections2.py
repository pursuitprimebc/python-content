'''QUESTION - Delete the first three elements in a list
Given a list l, modify it in place by deleting the first three elements. If the list has fewer than three elements, delete all elements.

Example

l = [1, 2, 3, 4, 5]
After deleting the first three elements, the list becomes [4, 5].
'''
# PLATFORM - IITM course 

def delete_first_three(l: list) -> None:
    del l[:3]
    
