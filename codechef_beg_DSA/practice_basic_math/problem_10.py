'''7 Rings
In Chefland, a valid phone number consists of 5 digits with no leading zeros.
For example,98765,10000, and 71023 are valid phone numbers while 04123,9231, and 872310 are not.

Chef went to a store and purchased N items, where the cost of each item is X.
Find whether the total bill is equivalent to a valid phone number.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of two space-separated integers N and X — the number of items Chef bought and the cost per item.
Output Format
For each test case, output on a new line, YES, if the total bill is equivalent to a valid phone number and NO otherwise.
'''


t = int(input())

while t > 0:
    n, x = map(int, input().split())
    t -= 1
    total_bill = str(n*x)
    if len(total_bill)==5 and total_bill[0]!='0':
        print('yes')
    else:
        print('no')

