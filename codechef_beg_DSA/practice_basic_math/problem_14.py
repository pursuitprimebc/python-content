''' QIESTION -Alternate Additions
Chef has 2 numbers A and B(A<B).

Chef will perform some operations on A.

In the ith  operation:

Chef will add 1 to A if i is odd.
Chef will add 2 to A if i is even.
Chef can stop at any instant. Can Chef make A equal to B?

Input Format
The first line contains a single integer T — the number of test cases. Then the test cases follow.
The first and only line of each test case contains two space separated integers A and B.
Output Format
For each test case, output YES if Chef can make A and B equal, NO otherwise.
'''


t = int(input())
for i in range(t):
    a,b = map(int, input().split())
    if (b - a) % 3 <= 1:
        print("YES")
    else:
        print("NO")
