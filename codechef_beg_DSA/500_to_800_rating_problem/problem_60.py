''' QUESTION - Airlines
An airline operates X aircraft every day. Each aircraft can carry up to 100 passengers.
One day, N passengers would like to travel to the same destination. What is the minimum number of new planes that the airline must buy to carry all N passengers?

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of a single line containing two space-separated integers X and N — the number of aircraft the airline owns and the number of passengers travelling, respectively.
Output Format
For each test case, output the minimum number of planes the airline needs to purchase.
'''


t = int(input())
for i in range(t):
    x,n = map(int, input().split())
    if n-(x*100)>0:
        if (n-(x*100))%100==0:
            print((n-(x*100))//100)
        else:
            print(((n-(x*100))//100)+1)
    else:
        print('0')


#  this above code was written by me but this below code was that which i learned during solving , both are correct but below one is more concise.


import math

t = int(input())
for i in range(t):
    x, n = map(int, input().split())
    remaining_passengers = n - (x * 100)
    if remaining_passengers > 0:
        needed_planes = math.ceil(remaining_passengers / 100)
        print(int(needed_planes))
    else:
        print(0)

        