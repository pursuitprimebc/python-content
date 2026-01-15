''' QUESTION - Exams
In Chefland, there are X schools, and each school has Y students.
The year end results are in and a total of Z students passed the exams.

Assuming that all students appeared for the exams, find whether the number of students who passed in Chefland was strictly greater than 50%.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of three space-separated integers X,Y, and Z, as mentioned in the statement.

Output Format
For each test case, output on a new line, YES, if the total number of students who passed in Chefland was strictly greater than 50%, otherwise print NO.
'''


t = int(input())
for i in range(t):
    x,y,z = map(int, input().split())
    total_student = x*y
    if z > (total_student//2):
        print('yes')
    else:
        print('no')
    




