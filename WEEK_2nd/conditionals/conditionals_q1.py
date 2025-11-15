'''Problem Type: Standard Output - Standard Output

You are tasked with creating a multi-purpose application that performs various operations based on user input. The application should take the operation name from the input and execute the corresponding task.

The operations your application should support are as follows:

Odd number checker: Check whether the input number is odd.
Name: odd_num_check
Inputs: number:int
Output: "yes" if the number is odd, "no" otherwise.
Perfect square checker: Check whether the input number is a perfect square.
Name: perfect_square_check
Inputs: number:int
Output: "yes" if the number is a perfect square, "no" otherwise.
Vowel checker: Check if a string has a vowel in it.
Name: vowel_check
Inputs: text:str
Output: "yes" if the string contains a vowel, "no" otherwise.
Divisibility checker: Check if a number is divisible by 2 or 3.
Name: divisibility_check
Inputs: number:int
Output: "divisible by 2" if the number is divisible by 2, "divisible by 3" if divisible by 3, "divisible by 2 and 3" if divisible by both, "not divisible by 2 and 3" otherwise.
Palindrominator: Takes a string and joins it with the same string reversed. Eg. "cal" -> "calac".
Name: palindrominator
Inputs: text:str
Output: string representing the input string joined with its reverse(the last characte should not be repeated twice)
Simple interest calculator with inputs with a higher interest rate if long term.
Name: simple_interest
Inputs: principal_amount:int, n_years:int (number of years)
Output: Simple interest with a 5% interest rate if less than 10 years, else 8%. Round the result to integer using round function.
If the operation name is not any of the above print "Invalid Operation".'''


import math
name = input()
y = 'yes'
n="no"
if name == "odd_num_check":
    num = int(input())
    if num%2 == 1:
        print(y)
    else:
        print(n)
            
elif name == 'perfect_square_check':
    num = int(input())
    if math.sqrt(num).is_integer():
        print(y)
    else:
        print(n)
            
elif name == "vowel_check":
    word = input().lower()
    if "a" in word or "e" in word or "i" in word or "o" in word or "u" in word:
        print(y)
    else:
        print(n)
        
elif name == "divisibility_check":
    num = int(input())
    if num%6 == 0:
        print("divisible by 2 and 3")
    elif num%2 == 0:
        print("divisible by 2")
    elif num%3 == 0:
        print("divisible by 3")
    else:
        print("not divisible by 2 and 3")
        
elif name == "palindrominator":
        word = input()
        rev_word = word[:len(word)-1]
        print(word+rev_word[::-1])
        
elif name == "simple_interest":
    principal_amount = int(input())
    n_year = int(input())
    rate=0.05 if n_year < 10 else 0.08
    interest = round(principal_amount * n_year * rate)
    print(interest)
else:
    print("Invalid operation")