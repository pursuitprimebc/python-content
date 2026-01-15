'''QUESTION - Reverse The Number
Given an Integer N, write a program to reverse it.

Input
The first line contains an integer T, total number of testcases. Then follow T lines, each line contains an integer N.

Output
For each test case, display the reverse of the given number N, in a new line.

Constraints
1 ≤ T ≤ 1000
1 ≤ N ≤ 1000000
'''



t = int(input())
for i in range(t):
    n = int(input())
    n = str(n)
    print(int(n[::-1]))
    
    
