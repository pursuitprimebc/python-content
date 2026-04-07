''' question - Find the peak elements in an array
Given an array A of size N, your task is to find and print all the peak elements in the array. A peak element is one that is strictly greater than its neighboring elements. For the first and last elements, only consider their single adjacent element.

If no peak element exists in the array, print -1.

Input Format
The first line contains the integer N — the size of array
The second line contains all the elements of array A
Output Format
Output all the peak elements in the array in the order they are present in the original array.
'''

# what i solved ---

# cook your dish here
n = int(input())
a = list(map(int, input().split()))
peaks = []

if n == 1:
    print(a[0])
    
for i in range(n):
    if i==0:
        if a[i] > a[i+1]: 
            peaks.append(a[i])
    
    elif i == (n-1):
        if a[n-1] > a[n-2]:
            peaks.append(a[n-1])
    
    else:
        if a[i] > a[i+1] and a[i] > a[i-1]:
            peaks.append(a[i])
            
if not peaks:
    print('-1')
else:
    print(*peaks)



# alternative approach (AI)
'''
n = int(input())
a = list(map(int, input().split()))

# Handle empty array case if necessary, though constraints say N >= 1
if n == 0:
    print("-1")
    exit()

peaks = []

for i in range(n):
    # Check left neighbor: valid if it's the first element or strictly greater than left
    is_greater_than_left = (i == 0) or (a[i] > a[i-1])
    
    # Check right neighbor: valid if it's the last element or strictly greater than right
    is_greater_than_right = (i == n-1) or (a[i] > a[i+1])
    
    if is_greater_than_left and is_greater_than_right:
        peaks.append(a[i])

if not peaks:
    print("-1")
else:
    print(*(peaks))
'''


# alternative approach [AI] 
'''
n = int(input())
A = list(map(int, input().split()))

peaks = [A[i] for i in range(n) if (i == 0 or A[i] > A[i-1]) and (i == n-1 or A[i] > A[i+1])]

print(*(peaks) if peaks else -1)
'''