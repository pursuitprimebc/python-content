'''QUESTION - Nearest Exit
There are two exits in a bus with 100 seats:

First exit is located beside seat number 1.
Second exit is located beside seat number 100.
Seats are arranged in a straight line from 1 to 100 with equal spacing between any 2 adjacent seats.

A passenger prefers to choose the nearest exit while leaving the bus.

Determine the exit taken by passenger sitting on seat X.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists a single integer X, denoting the seat number.
Output Format
For each test case, output LEFT if the passenger chooses the exit beside seat 1, RIGHT otherwise.
'''


t = int(input())
for i in range(t):
    x = int(input())
    if x<=50:
        print('left')
    else:
        print('right')






