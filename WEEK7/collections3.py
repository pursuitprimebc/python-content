'''QUESTIONS -  Number of unique common digits between two integers
Given two integers, return the number of unique digits that are common in both numbers.

Eg, 287498,295424 - 2, 4 and 9 are common to both nums so answer is 3
'''
#PLATFORM - IITM course

def number_of_unique_common_digits(n1: int, n2: int) -> int:
   
    digits_n1 = set(str(abs(n1)))
    digits_n2 = set(str(abs(n2)))
    
    return len(digits_n1 & digits_n2)
    
