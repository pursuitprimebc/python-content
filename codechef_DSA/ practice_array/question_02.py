''' QUESTION - Find maximum in an Array
Given a list of N integers, representing height of mountains. Find the height of the tallest mountain.

Input:
First line will contain T, number of testcases. Then the testcases follow.
The first line in each testcase contains one integer, N.
The following line contains N space separated integers: the height of each mountains.
Output:
For each testcase, output one line with one integer: the height of the tallest mountain for that test case.
'''


t = int(input())
for i in range(t):
    n = int(input())
    num = list(map(int, input().split())) 
    print(max(num))
    



