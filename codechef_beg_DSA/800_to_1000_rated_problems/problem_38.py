''' QUESTION - Count the Holidays
A particular month has 30 days, numbered from 1 to 30.

Day 1 is a Monday, and the usual 7-day week is followed (so day 2 is Tuesday, day 3 is Wednesday, and so on).

Every Saturday and Sunday is a holiday. There are N festival days, which are also holidays. Note that it is possible for a festival day to occur on a Saturday or Sunday.

You are given the dates of the festivals. Determine the total number of holidays in this month.

Input Format
The first line of input contains a single integer T, denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains an integer N denoting the number of festival days.
The second line of each test case contains N distinct space-separated integers A1,A2,…AN , denoting the festival days. Note that the Ai are not necessarily given in sorted order.
Output Format
For each test case, output a new line containing the total number of holidays
'''


t = int(input())
for i in range(t):
    n = int(input())
    a = list(input().split())
    weekends = ['6','7','13','14','20','21','27','28']
    count = 0
    for x in range(n):
        if a[x] in weekends:
            count += 1
    
    print((len(weekends))+(n-count))    


