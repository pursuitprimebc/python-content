'''QUESTION - Test Score
In a test, there are N problems, each carrying X marks.
In each problem, Chef either received X marks or 0 marks.

Determine whether is it possible for Chef to achieve exactly Y marks.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of three integers N,X, and Y, the number of problems, the maximum score for each problem, and the score Chef wants.
Output Format
For each test case, output YES if Chef can achieve exactly Y marks, NO otherwise.
'''


t = int(input())
for i in range(t):
    n,x,y = map(int, input().split())
    if (y%x==0 and y//x<=n) or y==0 and n!=0:
        print('yes')
    else:
        print('no')



