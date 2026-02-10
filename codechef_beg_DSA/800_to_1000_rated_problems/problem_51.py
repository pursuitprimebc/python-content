''' QUESTION - Am I Lucky!
A school has organized a field trip for a class of N students, of which X students are boys, and the remaining students are girls.
Everyone is excited to go trekking, and must form groups of size exactly K to do so. However, boys will only form groups among themselves, 
and girls will only form groups among themselves.
Both boys and girls will form as many groups as possible.

The remaining students can either dance around a bonfire, or just read books.
Dancing around the bonfire requires a pair of one girl and one boy, while reading is done alone.

Reading is much more boring than dancing, so students will try to avoid it.
What's the minimum number of students who will be engaged in reading?

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
The only line of each test case contains three space-separated integers N, X and K — the total number of students, the number of boys and the number of students in each trekking group.
Output Format
For each test case, output on a new line the the minimum number of students engaged in reading.
'''



t = int(input())
for i in range(t):
    n,x,k = map(int, input().split())
    # trekking groups
    b_grp = x//k
    g_grp = (n-x)//k 
    r_std = (x%k) + ((n-x)%k)
    # dancing groups
    pairs = min((x%k),((n-x)%k))
    students_involved = pairs*2
    # reading students
    rs = r_std - students_involved
    print(rs)



