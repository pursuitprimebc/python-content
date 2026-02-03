''' QUESTION - Circular Track
There is a circular track of length M consisting of M checkpoints and M bidirectional roads such that each road has a length of 1 unit.

--- imgage mentioned in previous .png file. ---

Chef is currently at checkpoint A and wants to reach checkpoint B. Find the minimum length of the road he needs to travel.

Input Format
First line will contain T, the number of test cases. Then the test cases follow.
Each test case contains a single line of input, three integers A,B, and M - the initial checkpoint, the final checkpoint, and the total number of checkpoints respectively.
Output Format
For each test case, output the minimum length Chef needs to travel.
'''



t = int(input())
for i in range(t):
    a,b,m = map(int, input().split())
    print(min((m-(abs(a-b))), abs(a-b)))
    
    


