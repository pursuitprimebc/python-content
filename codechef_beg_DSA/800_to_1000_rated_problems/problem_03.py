''' QUESTION - Buy 2 Get 1 Free
There is a sale going on in Chefland. For every 2 items Chef pays for, he gets the third item for free (see sample explanations for more clarity).

It is given that the cost of 1 item is X rupees. Find the minimum money required by Chef to buy at least N items.

Input Format
First line will contain T, number of test cases. Then the test cases follow.
Each test case contains of a single line of input, two integers N and X.
Output Format
For each test case, output the minimum money required by Chef to buy at least N items.
'''



t = int(input())
for i in range(t):
    n,x = map(int, input().split())
    no_of_paid_items = n-(n//3)
    minimum_cost = no_of_paid_items * x
    print(minimum_cost)    
    
