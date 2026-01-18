'''QUESTION - It is My Serve
Alice and Bob are playing a game of table tennis where irrespective of the point scored, every player makes 2 consecutive serves before the service changes. 
Alice makes the first serve of the match. Therefore the first 2 serves will be made by Alice, then the next 2 serves will be made by Bob and so on.

Let's consider the following example match for more clarity:

Alice makes the 1st serve.
Let us assume, Bob wins this point. (Score is 0 for Alice and 1 for Bob)
Alice makes the 2nd serve.
Let us assume, Alice wins this point. (Score is 1 for Alice and 1 for Bob)
Bob makes the 3rd serve.
Let us assume, Alice wins this point. (Score is 2 for Alice and 1 for Bob)
Bob makes the 4th serve.
Let us assume, Alice wins this point. (Score is 3 for Alice and 1 for Bob)Alice makes the 5th serve.
And the game continues… After the score reaches P and Q for Alice and Bob respectively, both the players forgot whose serve it is. Help them determine whose service it is.

Input Format
The first line contains a single integer T — the number of test cases. Then the test cases follow.
The first line of each test case contains two integers P and Q — the score of Alice and Bob respectively.
Output Format
For each test case, determine which player's (Alice or Bob) serve it is.
'''


t = int(input())
for i in range(t):
    p,q = map(int, input().split())
    sum_of_score = p+q
    A = True
    B = False
    serve = 1
    while serve <= sum_of_score:
        if serve == sum_of_score:
            break
        elif A == True:
            A=False 
            B=True
        else:
            A=True
            b=False
        serve+=2
    
    if A==True:
        print("Alice")
    else:
        print('Bob')
        
# this above code was written by me but this below code was what it should be precisely.

'''
The problem states that Alice serves first and each player serves for two consecutive turns. 
Therefore, we can determine the server by checking if the total number of serves (P + Q) divided by 2 is even or odd. If it's even, Alice is serving; otherwise, Bob is serving.
'''


t = int(input())
for _ in range(t):
    p, q = map(int, input().split())
    total_serves = p + q
    
    if (total_serves // 2) % 2 == 0:
        print("Alice")
    else:
        print("Bob")



