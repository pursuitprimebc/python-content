''' QUESTION - Inside The Stadium
Shubman Gill is playing an international match.
He played a total of N balls, where, in the ith ball, he scored Ai runs.

The strike rate of a player is calculated as :(no. of runs/no of balls played)x100.

Preet, a math enthusiast, is currently watching the match. Help him find the number of times, Shubman's strike rate became exactly 100.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of multiple lines of input.
The first line of each test case contains an integer N - the total number of balls played by Gill.
The second line of each test case contains N space-separated integers where Ai denotes runs scored on ith ball.
Output Format
For each test case, output on a new line, the total number of times the strike rate of Gill became 100.
'''


t = int(input())
for i in range(t):
    n = int(input())
    ai = list(map(int, input().split()))
    a=0
    count = 0
    run = 0 
    for  i in range(1,n+1):
        run += ai[a]
        sr = (run/i)*100
        if sr==100:
            count += 1
        a+=1
    
    print(count)
    



