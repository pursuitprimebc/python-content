''' QUESTION - Chef On Island
Suppose Chef is stuck on an island and currently he has x units of food supply and y units of water supply in total that he could collect from the island.
He needs xr units of food supply and yr units of water supply per day at the minimal to have sufficient energy to build a boat from the woods and also to live for another day.
Assuming it takes exactly D days to build the boat and reach the shore, tell whether Chef has the sufficient amount of supplies to be able to reach the shore by building the boat?

Input:
First line will contain T, number of testcases. Then the testcases follow.
Each testcase contains of a single line of input, five integers x,y,xr,yr,D.
Output:
For each testcase, output in a single line answer "YES" if Chef can reach the shore by building the boat and "NO" if not (without quotes).
'''


t = int(input())
for i in range(t):
    x,y,xr,yr,d = map(int, input().split())
    total_food_reqired = xr*d
    total_water_reqired = yr*d 
    if total_water_reqired<=y and total_food_reqired<=x:
        print('yes')
    else:
        print('no')



