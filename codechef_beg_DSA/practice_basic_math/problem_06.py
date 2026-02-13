''' QUESTION - Scalene Triangle
Given A,B, and C as the sides of a triangle, find whether the triangle is scalene.

Note:

A triangle is said to be scalene if all three sides of the triangle are distinct.
It is guaranteed that the sides represent a valid triangle.
Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of three space-separated integers A,B, and C — the length of the three sides of the triangle.
Output Format
For each test case, output on a new line, YES, if the triangle is scalene, and NO otherwise.
'''


t = int(input())

while t > 0:
    a, b, c = map(int, input().split())
    t -= 1
    if a!=b!=c:
        print('yes')
    else:
        print('no')




