''' QUESTION - Greater Average
You are given 3 numbers A,B, and C.

Determine whether the average of A and B is strictly greater than C or not?

NOTE: Average of A and B is defined as (A+B)/2 . For example, average of 5 and 9 is 7, average of 5 and 8 is 6.5.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of 3 integers A,B, and C.

Output Format
For each test case, output YES if average of A and B is strictly greater than C, NO otherwise.
'''


t = int(input())
for i in range(t):
    a,b,c = map(int, input().split())
    avg = (a+b)/2
    if avg > c:
        print('yes')
    else:
        print('no')
    
