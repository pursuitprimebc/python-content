''' QUESTION - Second Max of Three Numbers
Problem Statement
Write a program that accepts sets of three numbers, and prints the second-maximum number among the three.

Input
First line contains the number of triples, N.
The next N lines which follow each have three space separated integers.
Output
For each of the N triples, output one new line which contains the second-maximum integer among the three.
'''


n = int(input())
for i in range(n):
    x,y,z = map(int, input().split())
    if y<=x<=z or z<=x<=y:
        print(x)
    elif x<=y<=z or z<=y<=x:
        print(y)
    else:
        print(z)



