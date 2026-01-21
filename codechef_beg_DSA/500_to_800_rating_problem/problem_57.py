'''QUESTION - Chef Eren
Chef is a very big fan of Eren Yeager.

In the last season of Attack on Titan, there were N episodes numbered from 1 to N.
Each even indexed episode was A minutes long and each odd indexed episode was B minutes long.

Calculate the total duration (in minutes) of the last season.

Input Format
The first line of input contains a single integer T, the number of test cases.
The first and only line of each test case contains three integers N,A, and B, the number of episodes and the durations of each even-indexed and odd-indexed episodes respectively in minutes.
Output Format
For each test case, print a single integer on a new line, the total duration of the last season in minutes.
'''


t = int(input())
for i in range(t):
    n,a,b = map(int , input().split())
    total_score = 0
    for i in range(1,n+1):
        if i%2==0:
            total_score +=a 
        else:
            total_score +=b 
        
    print(total_score)
    
    

