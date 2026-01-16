'''QUESTION - Discus Throw
In discus throw, a player is given 3 throws and the throw with the longest distance is regarded as their final score.

You are given the distances for all 3 throws of a player. Dtermine the final score of the player.

Input Format
First line will contain T, number of test cases. Then the test cases follow.
Each test case contains of a single line of input, three integers A,B, and C denoting the distances in each throw.
Output Format
For each test case, output the final score of the player.
'''


t= int(input())
for i in range(t):
    a,b,c = map(int, input().split())
    finalscore = max(a,b,c)
    print(finalscore) 
    
    


