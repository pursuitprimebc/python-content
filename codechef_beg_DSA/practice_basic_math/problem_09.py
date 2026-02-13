''' QUESTION - Test Averages
Chef has scored A,B, and C marks in 3 different subjects respectively.

Chef will fail if the average score of any two subjects is less than 35. Determine whether Chef will pass or fail.

Input Format
First line will contain T, number of test cases. Then the test cases follow.
Each test case contains of a single line of input, three integers A,B,C, denoting the Chef's score in the three subjects.
Output Format
For each test case, if Chef will pass, print PASS, otherwise print FAIL.
'''


t = int(input())

while t > 0:
    a, b, c = map(int, input().split())
    t -= 1
    if ((a+b)/2)<35 or ((c+b)/2)<35 or ((a+c)/2)<35:
        print('fail')
    else:
        print('pass')

