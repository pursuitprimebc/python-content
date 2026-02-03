''' QUESTION - Smallest Numbers of Notes
Consider a currency system in which there are notes of six denominations, namely, Rs. 1, Rs. 2, Rs. 5, Rs. 10, Rs. 50, Rs. 100.
If the sum of Rs. N is input, write a program to compute smallest number of notes that will combine to give Rs. N.

Input

The first line contains an integer T, total number of testcases. Then follow T lines, each line contains an integer N.

Output
For each test case, display the smallest number of notes that will combine to give N, in a new line.
'''



t =  int(input())
for i in range(t):
    n = int(input())
    notes = 0
    while n!=0:
        notes = (n//100)
        n = n - ((n//100)*100)
        notes = notes + (n//50)
        n = n - ((n//50)*50)
        notes = notes + (n//10)
        n = n - ((n//10)*10)
        notes = notes + (n//5)
        n = n - ((n//5)*5)
        notes = notes + (n//2)
        n = n - ((n//2)*2)
        notes = notes + (n//1)
        n = n - ((n//1)*1)
    
    print(notes)


# this below is more optimized and readble which i got through ai .


t = int(input())
denominations = [100, 50, 10, 5, 2, 1]

for i in range(t):
    n = int(input())
    notes = 0
    for coin in denominations:
        notes += n // coin
        n %= coin
    print(notes)