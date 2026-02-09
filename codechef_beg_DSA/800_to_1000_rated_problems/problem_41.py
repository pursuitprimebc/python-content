''' question -HOW MANY DIGITS DO I HAVE
Write a program to obtain a number (N) from the user and display whether the number is a one digit number, 2 digit number, 3 digit number or more than 3 digit number

Input Format
First line will contain the number N,

Output Format
Print "1" if N is a 1 digit number.
Print "2" if N is a 2 digit number.
Print "3" if N is a 3 digit number.
Print "More than 3 digits" if N has more than 3 digits.
'''


n = int(input())
sn = str(n)
length = len(sn)
if length<4:
    print(length)
else:
    print('More than 3 digits')



