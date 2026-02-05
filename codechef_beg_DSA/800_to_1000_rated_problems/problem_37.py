''' QUESTION - Passing Marks
Read problems statements in Mandarin Chinese, Russian, and Bengali as well.
Recently, Chef's College Examination has concluded. He was enrolled in 3 courses and he scored A,B,C in them, respectively. To pass the semester, he must score at least Amin,Bmin ,Cmin
  marks in the respective subjects along with a cumulative score of at least, i.e, A+B+C≥Tmin .

Given seven integers Amin,Bmin,Cmin,Tmin ,A,B,C, tell whether Chef passes the semester or not.

###Input:

The first line will contain T, number of testcases. Then the testcases follow.
Each testcase contains of a single line of input, seven integers Amin,Bmin,Cmin,Tmin ,A,B,C each separated by aspace.
###Output: Output in a single line, the answer, which should be "YES" if Chef passes the semester and "NO" if not.
'''



t = int(input())
for i in range(t):
    Amin,Bmin,Cmin,Tmin,A,B,C = map(int, input().split())
    total_obt_marks = A+B+C
    if A>=Amin and B>=Bmin and C>=Cmin and total_obt_marks>=Tmin:
        print('yes')
    else:
        print('no')
    
    