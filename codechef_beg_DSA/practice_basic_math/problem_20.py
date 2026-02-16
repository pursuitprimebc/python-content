''' QUESTION - Construct N
You are given an integer N. Find if it is possible to represent N as the sum of several(possibly zero) 2's and several(possibly zero) 7's.

Formally, find if there exist two integers X,Y (X,Y≥0) such that 2⋅X+7⋅Y=N.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of a single line containing an integer N.
Output Format
For each test case, print on a new line YES if it is possible to represent N as the sum of several(possibly zero) 2's and several(possibly zero) 7's and NO otherwise.
'''


t = int(input())
for i in range(t):
    n = int(input())
    if n==1 or n==3 or n==5:
        print('no')
    else:
        print('yes')