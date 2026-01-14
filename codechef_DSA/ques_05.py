'''question - Pass the Exam
Chef appeared for an exam consisting of3 sections. Each section is worth 100 marks.Chef scored A marks in Section 1, B marks in section 2, and C marks in section 3.
Chef passes the exam if both of the following conditions satisfy:
Total score of Chef is ≥100;
Score of each section ≥10.
Determine whether Chef passes the exam or not.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of a single line containing 3 space-separated numbers A,B,C - Chef's score in each of the sections.
Output Format
For each test case, output 'PASS' if Chef passes the exam, 'FAIL' otherwise.
'''

t=int(input())
for i in range(t):
    A, B, C = map(int,input().split())
    total_score = A + B + C
    minimum_score = min(A,B,C)
    if total_score>=100 and minimum_score>=10:
        print('PASS')
    else:
        print('FAIL')