''' QUESTION - Janmansh and Assignments
Janmansh has to submit 3 assignments for Chingari before 10 pm and he starts to do the assignments at X pm.
Each assignment takes him 1 hour to complete. Can you tell whether he'll be able to complete all assignments on time or not?

Input Format
The first line will contain T - the number of test cases. Then the test cases follow.
The first and only line of each test case contains one integer X - the time when Janmansh starts doing the assignments.

Output Format
For each test case, output Yes if he can complete the assignments on time. Otherwise, output No.
'''


t = int(input())
for i in range(t):
    x = int(input())
    time_taken = x+3
    if time_taken > 10:
        print('no')
    else:
        print('yes')
    


