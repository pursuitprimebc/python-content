'''Largest and Second Largest
You are given an array A of N integers.
Find the maximum sum of two distinct integers in the array.

Note: It is guaranteed that there exist at least two distinct integers in the array.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of multiple lines of input.
The first line of each test case contains single integer N — the size of the array.
The next line contains N space-separated integers, denoting the array A.
Output Format
For each test case, output on a new line, the maximum sum of two distinct integers in the array.
'''


t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    t -= 1
    
    max1 = max(a)
    remaining_distinct = [x for x in a if x != max1]
    max2 = max(remaining_distinct)
    
    print(max1 + max2)
