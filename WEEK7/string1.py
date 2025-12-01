'''QUESTION - Check if all the odd indices are alphabets and even indices are digits
Given a string, check if all the odd indices are alphabets and the even indices are digits.

Note: indices starts from 0.'''
# PLATFORM - IITM course

def is_odd_indices_alpha_and_even_indices_digits(string: str) -> bool:
    for i in range (len(string)):
        if i % 2 == 0:
            if not string[i].isdigit():
                return False
        else:
            if not string[i].isalpha():
                return False
                
    return True
    
