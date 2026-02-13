''' QUESTION - Sum of Digits
You're given an integer N. Write a program to calculate the sum of all the digits of N.

Input Format
The first line contains an integer T, the total number of testcases. Then follow T lines, each line contains an integer N.

Output Format
For each test case, calculate the sum of digits of N, and display it in a new line.

'''


t = int(input())
for i in range(t):
    n = input()
    digit_sum = sum(int(digit) for digit in (n))
    print(digit_sum)
