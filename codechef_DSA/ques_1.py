'''QUESTION - Practice problem - Burgers
Chef has A patties and B buns.To make 1 burger, Chef needs 1 patty and 1 bun.
Find the maximum number of burgers that Chef can make.

Input Format
The first line of input will contain an integer T — the number of test cases.
The first and only line of each test case contains two space-separated integers A and B, the number of patties and buns respectively.

Output Format
For each test case, output the maximum number of burgers that Chef can make.
'''
# PLATFORM - CodeChef




t = int(input())            
for i in range(t):          
    #Accept 2 integers inputs.
    A, B = map(int,input().split())    
    Burgers = 0
    if A>B:
        Burgers+=B
    else:
        Burgers+=A
    print('No. of burgers made: ', Burgers)                

