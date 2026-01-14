'''QUESTION - Problem (Make Avg) 
You are given 2 integers - A and C.
You need to find if there exists any integer B which meets the following condition B must be an integerB is the average of A and C.
Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of two space-separated integers A and C, the given integers.
Output Format
For each test case, output -1 if there exists no integer B such that A,B, and C are in arithmetic progression. Else, output the value of B.
'''

t = int(input())            
for i in range(t):          
    A, C = map(int, input().split())
    if (A+C)%2==0:
        B = (A+C)//2
        print(B)
    else:
        print('-1')
    


