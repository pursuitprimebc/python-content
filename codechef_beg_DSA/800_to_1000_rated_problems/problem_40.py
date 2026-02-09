''' QUESTION - Problem
One less problem without ya
I got one less problem without ya

Alice and Bob are competing in a challenge. Initially Alice has N problems and Bob has M problems.

Each time Alice solves a problem, Bob receives one more problem to solve.
Each time Bob solves a problem, Alice receives three more problems to solve.
Find whether it is possible that both of them have the same number of problems left if they can solve the problems in any arbitrary manner.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case contains two space-separated integers N and M — the initial number of problems of Alice and Bob respectively.
Output Format
For each test case, output on a new line, YES, it is possible that both of them have the same number of problems left if they can solve the problems in any arbitrary manner and NO otherwise.
'''



t = int(input())
for i in range(t):
    n,m = map(int, input().split())
    if abs(n-m)%2==0:
        print('yes')
    else:
        print('no')



