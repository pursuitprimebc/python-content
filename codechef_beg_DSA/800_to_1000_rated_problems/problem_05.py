''' QUESTION - The Preparations
Chef has an exam which will start exactly M minutes from now. However, instead of preparing for his exam, Chef started watching Season-1 of Superchef. 
Season-1 has N episodes, and the duration of each episode is K minutes.

Will Chef be able to finish watching Season-1 strictly before the exam starts?

Input Format
The first line contains an integer T denoting the number of test cases. T test cases then follow.
The first and only line of each test case contains 3 space separated integers M,N and K.
Output Format
For each test case, output on one line YES if it is possible to finish Season-1 strictly before the exam starts, or NO if it is not possible to do so.
'''



t = int(input())
for i in range(t):
    m,n,k = map(int, input().split())
    duration_of_season = n * k 
    if duration_of_season < m:
        print('yes')
    else:
        print('no')
    

