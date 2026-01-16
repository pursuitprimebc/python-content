''' QUESTION - Chess Ratings
Alice has recently started playing Chess. Her current rating is X. She noticed that when she wins a game, her rating increases by 8 points.

Can you help Alice in finding out the minimum number of games she needs to win in order to make her rating greater than or equal to Y?

Input Format
The first line of input will contain an integer T — the number of test cases. The description of T test cases follows.
The first line of each test case contains two integers X and Y, as described in the problem statement.
Output Format
For each test case, output the minimum number of games that Alice needs to win in order to make her rating greater than or equal toY.
'''


t = int(input())
for i in range(t):
    x,y = map(int, input().split())
    increased_rating = y-x
    if increased_rating%8!=0:
        print((increased_rating//8)+1)
    else:
        print(increased_rating//8)


# this above code was written by me but this below code was that which i learned during solving , both are correct but below one is more concise.


import math

t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    increased_rating = y - x
    print(math.ceil(increased_rating / 8))


''' Here's a breakdown of the changes and why they're helpful:

import math: This line imports the math module, which contains the ceil function.
math.ceil(increased_rating / 8): This calculates the ceiling of the result of increased_rating / 8. 
The ceiling function rounds a number up to the nearest integer. For example, math.ceil(7.2) would return 8.
'''