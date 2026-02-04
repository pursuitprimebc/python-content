''' question - Car Choice
Chef is planning to buy a new car for his birthday. After a long search, he is left with 2 choices:

Car 1: Runs on diesel with a fuel economy of x1 km/l
Car 2: Runs on petrol with a fuel economy of x2 km/l
Chef also knows that

the current price of diesel is y1
  rupees per litre
the current price of petrol is y2
  rupees per litre
Assuming that both cars cost the same and that the price of fuel remains constant, which car will minimize Chef's expenses?

Print your answer as a single integer in the following format

If it is better to choose Car 1, print -1
If both the cars will result in the same expenses, print 0
If it is better to choose Car 2, print 1
Input Format
The first line of input contains a single integer T, denoting the number of test cases. The description of T test cases follows.
Each test case consists of a single line containing 4 space-separated integers — x1,x2 ,y1,y2
 .
Output Format
For each test case, output in a single line the answer as explained earlier.
'''



t = int(input())
for i in range(t):
    x1,x2,y1,y2 = map(int, input().split())
    cost_per_km_in_car1 = (y1/x1)
    cost_per_km_in_car2 = (y2/x2)
    if cost_per_km_in_car2<cost_per_km_in_car1:
        print('1')
    elif cost_per_km_in_car1<cost_per_km_in_car2:
        print('-1')
    else:
        print('0')


