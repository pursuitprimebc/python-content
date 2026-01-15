'''QUESTION - Air Conditioner Temperature
There are three people sitting in a room - Alice, Bob, and Charlie. They need to decide on the temperature to set on the air conditioner. Everyone has a demand each:

Alice wants the temperature to be at least A degrees.
Bob wants the temperature to be at most B degrees.
Charlie wants the temperature to be at least C degrees.
Can they all agree on some temperature, or not?

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of a single line which contains three integers - A,B,C.
Output Format
For each test case, output on a new line, "Yes" or "No". "Yes", if they can decide on some temperature which fits all their demands. Or "No", if no temperature fits all their demands.
'''


t = int(input())
for i in range(t):
    a,b,c = map(int, input().split()) 
    if a>b or c>b:
        print('no')
    else:
        print('yes')




