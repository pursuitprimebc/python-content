'''
Merge two sorted arrays
You are given two sorted arrays A and B of size N and M respectively. You need to merge these two arrays and keep the final array sorted.

Input Format
The first line contains two integers N and M — the size of array A and B
The second line contains all the elements of array A
The third line contains all the elements of array B
Output Format
Output the merged array elements on a single line.
'''


n, m = map(int, input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
i,j=0,0
nlist = []

while i < len(A) and j < len(B):
    if A[i] <= B[j]:
        nlist.append(A[i])
        i += 1
    else:
        nlist.append(B[j])
        j += 1
while i < len(A):
    nlist.append(A[i])
    i += 1
while j < len(B):
    nlist.append(B[j])
    j += 1
    
print(*nlist)