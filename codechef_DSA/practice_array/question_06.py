''' question - MIN To MAX
You are given an array A of size N.

Let M be the minimum value present in the array initially.
In one operation, you can choose an element Ai(1≤i≤N) and an integer X(1≤X≤100), and set Ai =X.

Determine the minimum number of operations required to make M the maximum value in the array A.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of multiple lines of input.
The first line of each test case contains a single integer N - the size of the array.
The next line of each test case contains N space-separated integers A1,A2,…,AN - the elements of the array.
Output Format
For each test case, output on a new line, the minimum number of operations required to make M the maximum value in the array A
'''


def count_non_minimum(nums):
    n = len(nums)
    m = min(nums)
    count_m = 0
    for x in nums:
        if x == m:
            count_m += 1
    
    return n - count_m
        
t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    
    print(count_non_minimum(nums))


