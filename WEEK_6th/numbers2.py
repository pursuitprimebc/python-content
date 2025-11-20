'''QUESTION - Check if ten digit even number
Write a function to check if a number is a ten-digit even number.
Also account for negative numbers discarding the sign.

Examples

>>> is_ten_digit_even(8769473839)
False
>>> is_ten_digit_even(928948)
False
>>> is_ten_digit_even(9289479278)
True
>>> is_ten_digit_even(-9289479278)
True
'''
# PLATFORM - IITM COURSE

def is_ten_digit_even(n):
    abs_n = abs(n)
    
    if abs_n <1000000000 or abs_n > 9999999999:
        return False
        
    return abs_n % 2 == 0

    