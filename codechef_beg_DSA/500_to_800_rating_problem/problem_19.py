'''QUESTION - Monopoly
There are 4 companies in the markets of Chefland, A, B, C, and D.
This year,

Company A made a profit of P lakh rupees,
Company B made a profit of Q lakh rupees,
Company C made a profit of R lakh rupees,
Company D made a profit of S lakh rupees.
There is said to be a monopoly in the market if the profit made by one company is strictly greater than the sum of profits made by all other companies.
Determine if there is a monopoly in the market or not.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
The first line and only line of each test case contains four space-separated integers P, Q, R and S — the profits made by companies A, B, C and D respectively.
Output Format
For each test case, output YES if there is a monopoly in the market. Otherwise, output NO.
'''


t = int(input())
for i in range(t):
    p,q,r,s = map(int, input().split())
    A = (p-(q+r+s))
    B = (q-(p+r+s))
    C = (r-(p+q+s))
    D = (s-(p+q+r))
    if A>0 or B>0 or C>0 or D>0:
        print('yes')
    else:
        print('no')


