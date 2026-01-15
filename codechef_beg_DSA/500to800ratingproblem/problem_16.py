'''QUESTION - Car or Bike
Chef wants to reach home as soon as possible. He has two options:

Travel with his BIKE which takes X minutes.
Travel with his CAR which takes Y minutes.
Which of the two options is faster or do they both take same time?

Input Format
First line will contain T, number of test cases. Then the test cases follow.
Each test case contains a single line of input, two integers X,Y representing the time taken to travel with BIKE and CAR respectively.
Output Format
For each test case, print CAR if travelling with Car is faster, BIKE if travelling with Bike is faster, SAME if they both take the same time.
'''


t = int(input())
for i in range(t):
    x,y = map(int, input().split())
    if x>y:
        print('car')
    elif x==y:
        print('same')
    else:
        print('bike')
    


