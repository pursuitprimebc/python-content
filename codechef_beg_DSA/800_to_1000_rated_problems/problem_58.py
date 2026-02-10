''' QUESTION - Kitchen Timetable
Read problems statements in Mandarin Chinese, Russian and Vietnamese as well.
There are N students living in the dormitory of Berland State University. Each of them sometimes wants to use the kitchen, so the head of the dormitory came up with a timetable for kitchen's usage in order to avoid the conflicts:

The first student starts to use the kitchen at the time 0 and should finish the cooking not later than at the time A1.
The second student starts to use the kitchen at the time A1 and should finish the cooking not later than at the time A2.
And so on.
The N-th student starts to use the kitchen at the time AN-1 and should finish the cooking not later than at the time AN
The holidays in Berland are approaching, so today each of these N students wants to cook some pancakes. The i-th student needs Bi units of time to cook.

The students have understood that probably not all of them will be able to cook everything they want. How many students will be able to cook without violating the schedule?

Input Format
The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.
Each test case contains 3 lines of input

The first line of each test case contains a single integer N denoting the number of students.
The second line contains N space-separated integers A1, A2, ..., AN denoting the moments of time by when the corresponding student should finish cooking.
The third line contains N space-separated integers B1, B2, ..., BN denoting the time required for each of the students to cook.
Output Format
For each test case, output a single line containing the number of students that will be able to finish the cooking.
'''


t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if i==0:
            if a[i]>=b[i]:
                count+=1 
        else:
            if (a[i]-a[i-1])>=b[i]:
                count +=1
        
    print(count)


