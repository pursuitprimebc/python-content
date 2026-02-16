''' QUESTION - Make A and B equal
Chef has two numbers A andB.

In one operation, Chef can choose either A or B and multiply it by 2.

Determine whether he can make both A and B equal after any number (possibly, zero) of moves.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of two space-separated integers A and B.
Output Format
For each test case, output YES if Chef can make both numbers equal, NO otherwise.
'''


t = int(input())
for i in range(t):
    a,b = map(int, input().split())
    x = min(a,b)
    y = max(a,b)
    while x<y:
       x = x*2
    
    if x==y:
        print('yes')
    else:
        print('no')
            