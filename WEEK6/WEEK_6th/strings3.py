'''QUESTION - Palindrome Integer
Given an integer, check whether it is a palindrome. A palindrome is a number or a string that reads the same backward as forward.

Assume the numbers are positive.

Example

is_palindrome(121) == True
is_palindrome(123) == False
is_palindrome(1212) == False
'''
# PLATFORM - IITM course

ef is_palindrome(n: int) -> bool:
    str_n = str(n)
    return str_n == str_n[::-1]