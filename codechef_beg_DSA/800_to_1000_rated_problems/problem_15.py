''' QUESTION - Equal Integers
Chef has two integers X and Y. Chef wants to perform some operations to make X and Y equal. In one operation, Chef can either:
set X:=X+1 or 
set Y:=Y+2
Find the minimum number of operations required to make X and Y equal.

Input Format
The first line contains a single integer T — the number of test cases. Then the test cases follow.
The first and only line of each test case contains two space separated integers X and Y.
Output Format
For each test case, print the minimum number of operations required to make X and Y equal.
'''



import math

t = int(input())
for i in range(t):
    x,y = map(int, input().split())
    if y>=x:
        print(y-x)
    else:
        if (x-y)%2==0:
            print(math.ceil((x-y)/2))
        else:
            print(math.ceil((x-y)/2)+1)


