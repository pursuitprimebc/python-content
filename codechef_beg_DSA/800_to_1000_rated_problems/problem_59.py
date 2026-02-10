''' QUESTION - Bear and Ladder
Read problems statements in Mandarin Chinese, Russian and Vietnamese as well.
Bearland has infinitely many cities, numbered starting from 1. Some pairs of cities are connected with bidirectional roads:

There are roads 1-2, 3-4, 5-6, 7-8, and so on (there is a road between cities 2*i+1 and 2*i+2 for every non-negative integer i).
There are roads 1-3, 3-5, 5-7, 7-9, ... (between every two consecutive odd numbers).
There are roads 2-4, 4-6, 6-8, 8-10, ... (between every two consecutive even numbers).


You are given Q queries. In each query, for the given pair of different cities a and b, you should check if there is a road between them. For each query, print "YES" or "NO" accordingly.

Input
The first line of the input contains an integer Q, denoting the number of queries.

Each of the following Q lines contains two distinct integers a and b, denoting two cities in one query.

Output
For each query, output a single line containing the answer — "YES" if there is a road between the given cities a and b, and "NO" otherwise (without the quotes).
'''


q = int(input())
for i in range(q):
    a,b = map(int,input().split())
    if a%2==0:
        if (a-1)==b or (a+2)==b or (a-2)==b:
            print('yes')
        else:
            print('no')
    else:
        if (a+1)==b or (a-2)==b or (a+2)==b:
            print('yes')
        else:
            print('no')




