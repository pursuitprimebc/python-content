''' QUESTION - Candy Store
Chef has started working at the candy store. The store has 100 chocolates in total.

Chef’s daily goal is to sell X chocolates. For each chocolate sold, he will get 1 rupee. However, if Chef exceeds his daily goal, he gets 2 rupees per chocolate for each extra chocolate.

If Chef sells Y chocolates in a day, find the total amount he made.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of two space-separated integers X and Y — the daily goal of Chef, and the number of chocolates he actually sells.
Output Format
For each test case, output on a new line the total amount Chef made in a day.
'''



t = int(input())

while t > 0:
    x, y = map(int, input().split())
    t -= 1
    if y>x:
        print(((y-x)*2)+x)
    else:
        print(y)
