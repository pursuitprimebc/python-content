''' UESTION- Equalizing Numbers
Chef has two integers A and B. In one operation he can choose any integer d, and make one of the following two moves :

Add d to A and subtract d from B.
Add d to B and subtract d from A.
Chef is allowed to make as many operations as he wants. Can he make A and B equal?

Input Format
First line will contain T, number of test cases. Then the test cases follow.
Each test case contains of a single line of input, two integers A,B.
Output Format
For each test case, if Chef can make the two numbers equal print YES else print NO.
'''


for i in range(t):
    a ,b = map(int, input().split())
    if (abs(a-b))%2==0:
        print('yes')
    else:
        print('no')

