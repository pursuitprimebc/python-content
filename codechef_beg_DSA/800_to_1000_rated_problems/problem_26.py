''' QUESTION - Counting Pretty Numbers
Read problems statements in Mandarin chinese, Russian and Vietnamese as well.
Vasya likes the number 239. Therefore, he considers a number pretty if its last digit is 2,3 or 9.

Vasya wants to watch the numbers between L and R (both inclusive), so he asked you to determine how many pretty numbers are in this range. Can you help him?

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first and only line of each test case contains two space-separated integers L and R.
Output
For each test case, print a single line containing one integer — the number of pretty numbers between L and R.
'''


t = int(input())
for i in range(t):
    l,r = map(int , input().split())
    count = 0
    for i in range(l,r+1):
        i = str(i)
        if i[len(i)-1]=='2' or i[len(i)-1]=='3' or i[len(i)-1]=='9':
            count = count + 1
            
    print(count)



