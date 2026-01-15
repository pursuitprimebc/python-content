'''QUESTION - Qualify the round
In a coding contest, there are two types of problems:

Easy problems, which are worth 1 point each
Hard problems, which are worth 2 points each
To qualify for the next round, a contestant must score at least X points. Chef solved A Easy problems and B Hard problems. Will Chef qualify or not?

Input Format
The first line of input contains a single integer T, denoting the number of test cases. The description of T test cases follows.
Each test case consists of a single line of input containing three space-separated integers — X,A, and B.
Output Format
For each test case, output a new line containing the answer — Qualify if Chef qualifies for the next round, and NotQualify otherwise.
'''


t = int(input())
for i in range(t):
    x,a,b = map(int, input().split())
    if a+(b*2)>=x:
        print('qualify')
    else:
        print('notqualify')
    


