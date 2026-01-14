''' QUESTION - Too many Floors
Chef and Chefina are residing in a hotel.

There are 10 floors in the hotel and each floor consists of 10 rooms.
Floor 1 consists of room numbers 1 to 10.
Floor 2 consists of room numbers 11 to 20.
…
Floor i consists of room numbers 10⋅(i-1)+1 to 10⋅i.
You know that Chef's room number is X while Chefina's Room number is Y.
If Chef starts from his room, find the number of floors he needs to travel to reach Chefina's room.

Input Format
First line will contain T, number of test cases. Then the test cases follow.
Each test case contains of a single line of input, two integers X,Y, the room numbers of Chef and Chefina respectively.
Output Format
For each test case, output the number of floors Chef needs to travel to reach Chefina's room.
'''


t= int(input())
for i in range(t):
    x,y = map(int, input().split())
    if x%10==0:
        chefs_floor = (x//10)
    else:
        chefs_floor = (x//10)+1 
        
    if y%10==0:
        chefinas_floor = (y//10)
    else:
        chefinas_floor = (y//10)+1
    
    if chefs_floor >= chefinas_floor:
        print(chefs_floor - chefinas_floor)
    else:
        print(chefinas_floor - chefs_floor)
    
    
