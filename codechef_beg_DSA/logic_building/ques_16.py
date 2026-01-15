'''QUESTION - A or B
There are two problems in a contest.

Problem A is worth 500 points at the start of the contest.
Problem B is worth 1000 points at the start of the contest.
Once the contest starts, after each minute:

Maximum points of Problem A reduce by 2 points .
Maximum points of Problem B reduce by 4 points.
It is known that Chef requires X minutes to solve Problem A correctly and Y minutes to solve Problem B correctly.
Find the maximum number of points Chef can score if he optimally decides the order of attempting both the problems.

Input Format
First line will contain T, number of test cases. Then the test cases follow.
Each test case contains of a single line of input, two integers X and Y - the time required to solve problems A and B in minutes respectively.

Output Format
For each test case, output in a single line, the maximum number of points Chef can score if he optimally decides the order of attempting both the problems.
'''


t = int(input())
for i in range(t):
    x,y = map(int, input().split())
    # from A to B 
    maximum_points_AB = (500-(x*2)) + (1000-((x+y)*4))
    # from B to A 
    maximum_points_BA = (1000-(y*4)) + (500-((y+x)*2))
    print(max(maximum_points_AB, maximum_points_BA))
    
    

