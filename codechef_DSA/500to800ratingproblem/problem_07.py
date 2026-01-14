''' QUESTION - CRED Coins
For each bill you pay using CRED, you earn X CRED coins.
At CodeChef store, each bag is worth 100 CRED coins.

Chef pays Y number of bills using CRED. Find the maximum number of bags he can get from the CodeChef store.

Input Format
First line will contain T, number of test cases. Then the test cases follow.
Each test case contains of a single line of input, two integers X and Y.
Output Format
For each test case, output in a single line - the maximum number of bags Chef can get from the CodeChef store.

Constraints
1≤T≤100
1≤X,Y≤1000

Subtasks
Subtask 1 (100 points): Original constraints.
'''


t = int(input())
for i in  range(t):
    x,y = map(int, input().split())
    coins_earned = x*y
    no_of_bags = coins_earned//100
    print(no_of_bags)



