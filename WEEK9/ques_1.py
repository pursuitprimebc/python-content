# QUESTION - Write a recursive function named reverse that accepts a list L as argument and returns the reversed list.
# PLATFORM - IITM Course

def reverse(L):
   
    if len(L)==0:
        return []
    return [L[-1]]+reverse(L[:-1])


