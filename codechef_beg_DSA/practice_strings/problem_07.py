''' QUESION - Add One
You are given a large number N. You need to print the number N+1.

Note: The number is very large and it will not fit in standard integer data type. You have to take the input as String and then manipulate the digits to convert it to N+1.

Input Format
The first line of the input contains a single integer T - the number of test cases. The description of T test cases follows.

The first line of each test case contains a single integer N.

Output Format
For each test case, print a single line string - the number N+1.
Constraints
1≤T≤100
1≤N≤10^200000-1
the sum of the number of digits of all N in a single test file does not exceed 4⋅10^5
 
Subtasks
Subtask #1 (30 points):
each digit of the number N is at most 8
Subtask #2 (70 points): original constraints
'''


t = int(input())
for i in range(t):
    n = input()
    N = ""
    for i in range(len(n)):
        if n[(len(n)-1)-i]=='9':
            N = '0' + N
        else:
            N = str(int(n[(len(n)-1)-i])+1) + N
            N = n[:-(i+1)] + N 
            break
    if N == (len(n)*'0'):
        N = '1' + N 
    print(N)
    
    