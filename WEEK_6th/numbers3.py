'''QUESTION - Arithmetic Operations tuple from two integers
Given a tuple of two integers (a, b), return a tuple containing the sum, difference, product, and quotient (integer division) of the two numbers.
Example:

>>> arithmetic_operations((1, 2))
(3, -1, 2, 0)
'''
# PLATFORM - IITM course

def arithmetic_operations(t: tuple) -> tuple:
    a, b = t
    
    sum_result = a +b
    difference = a-b
    product = a*b
    quotient = a//b
    
    return (sum_result,difference,product,quotient)
