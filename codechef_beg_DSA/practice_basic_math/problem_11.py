''' QUESTION - Make AP
Chef is given two integers A and C such that A≤C.

Chef wants to find whether there exists any integer B such that A,B, and C are in arithmetic progression.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of two space-separated integers A and C, the given integers.
Output Format
For each test case, output -1 if there exists no integer B such that A,B, and C are in arithmetic progression. Else, output the value of B.
'''


t = int(input())

while t > 0:
    a, c = map(int, input().split())
    t -= 1
    if (a+c)%2==0:
        print((a+c)//2)
    else:
        print('-1')

