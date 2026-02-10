''' QUESTION - Non-Negative Product
Alice has an array of N integers — A1,A2,…,AN . She wants the product of all the elements of the array to be a non-negative integer. 
That is, it can be either 0 or positive. But she doesn't want it to be negative.

To do this, she is willing to remove some elements of the array. Determine the minimum number of elements that she will have to remove 
to make the product of the array's elements non-negative.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
The first line of each test case contains a single integer N — the number of elements in the array originally.
The next line contains N space-separated integers — A1,A2,…,AN , which are the original array elements.
Output Format
For each test case, output on a new line the minimum number of elements that she has to remove from the array.
'''



t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    p = 1
    for i in (a):
        if i<0:
            count+=1
        p *= i 
        
    if count%2==0 or p==0:
        print(0)
    else:
        print(count%2)



