'''QUESTION - Air Hockey
Alice is playing Air Hockey with Bob. The first person to earn seven points wins the match. Currently, Alice's score is
A and Bob's score is B.
Charlie is eagerly waiting for his turn. Help Charlie by calculating the minimum number of points that will be further scored in the match before it ends.

Input Format
The first line of input will contain an integer T — the number of test cases. The description of 
T test cases follows.The first and only line of each test case contains two space-separated integers A and 
B, as described in the problem statement.

Output Format
For each test case, output on a new line the minimum number of points that will be further scored in the match before it ends.

Constraints
1≤T≤50
0≤A,B≤6
'''

t = int(input())
for i in range(t):
    a , b = map(int, input().split())
    maximum = max(a,b)
    minimum_points_required = 7 - maximum
    print(minimum_points_required)


# EXPLANATION = 