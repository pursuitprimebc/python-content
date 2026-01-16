'''QUESTION - Mario and Bullet
Mario's bullet moves at X pixels per frame. He wishes to shoot a goomba standing Y pixels away from him. The goomba does not move.

Find the minimum time (in seconds) after which Mario should shoot the bullet, such that it hits the goomba after at least Z seconds from now.

Input Format
The first line of input will contain an integer T, the number of test cases. Then the test cases follow.
Each test case consists of a single line of input, containing three space-separated integersX,Y, and Z.
Output Format
For each test case, output in a single line the minimum time (in seconds) after which Mario should shoot the bullet, such that it hits the goomba after at least Z seconds from now.
'''


t = int(input())
for i in range(t):
    x,y,z = map(int, input().split())
    time_to_reach_goomba = y//x
    if time_to_reach_goomba > z or time_to_reach_goomba == z :
        print('0')
    else:
        print(z- time_to_reach_goomba)
    



