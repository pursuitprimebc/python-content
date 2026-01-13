''' QUESTION - Minimum number of coins
Chef has infinite coins in denominations of rupees 5 and rupees 10.

Find the minimum number of coins Chef needs, to pay exactly X rupees. If it is impossible to pay X rupees in denominations of rupees 5 and 10 only, print -1.

Input Format
First line will contain T, number of test cases. Then the test cases follow.
Each test case contains of a single integer X.

Output Format
For each test case, print a single integer - the minimum number of coins Chef needs, to pay exactly 
X rupees. If it is impossible to pay X rupees in denominations of rupees 5 and 10 only, print -1.
'''


t = int(input())
for i in range(t):
    x= int(input())
    if x%5==0 or x%10==0:
        if x<10:
            print(x//5)
        else:
            if x%10==0:
                print(x//10)
            else:
                print((x//10)+1)
    else:
        print('-1')


