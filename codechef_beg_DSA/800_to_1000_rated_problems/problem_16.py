''' QUESTION - Summer Heat

Chefland has 2 different types of coconut, type A and type B. Type A contains only xa
milliliters of coconut water and type B contains only xb
grams of coconut pulp. Chef's nutritionist has advised him to consume Xa milliliters of coconut water and Xb
grams of coconut pulp every week in the summer. Find the total number of coconuts (typeA + typeB) that Chef should buy each week to keep himself active in the hot weather.

Input Format
The first line contains an integer T, the number of test cases. Then the test cases follow.
Each test case contains a single line of input, four integers xa,xb, Xa,Xb .
Output Format
For each test case, output in a single line the answer to the problem.
'''


import math

t = int(input())
for i in range(t):
    xa,xb,Xa,Xb = map(int, input().split())
    no_of_typeA_coconut = (math.ceil(Xa/xa))
    no_of_typeB_coconut = (math.ceil(Xb/xb))
    total = no_of_typeB_coconut+no_of_typeA_coconut
    print(total)




