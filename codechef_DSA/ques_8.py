'''QUESTION - Change Row and Column Both
There is a 10x10 grid with rows numbered 1 to 10 from top to bottom, and columns 1 to 10 from left to right.
Each cell is identified by a pair (r,c) which means that the cell is located at row r and column c.

If Chef's current location is(a,b), then in one move Chef can go to (c,d) if both of the following are satisfied:
a≠c
b≠d
Determine the minimum number of moves required to go from (sx,sy) to (ex,ey).

Input Format
The first line contains a single integer T — the number of test cases. Then the tst cases follow.
The first and only line of each test case contains four integer sx, sy, ex, ey — the coordinates of the starting and ending cells.
Output Format
For each testcase, output the minimum number of moves required to go from (sx,sy) to (ex,ey).
'''



t = int(input())
for i in range(t):
    a,b,c,d = map(int, input().split())
    if a!=c and b!=d:
        print('1')
    else:
        print('2')

