''' QUESTION - Weights
Chef is playing with weights. He has an object weighing W units. He also has three weights each of X,Y, and Z units respectively. Help him determine whether he can measure 
the exact weight of the object with one or more of these weights.

If it is possible to measure the weight of object with one or more of these weights, print YES, otherwise print NO.

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of single line containing a four positive integers W,X,Y, and Z.
Output Format
For each test case, output on a new line YES if it is possible to measure the weight of object with one or more of these weights, otherwise print NO.
'''


t = int(input())
for i in range(t):
    w, x, y, z = map(int, input().split())
    possible_weights = {x, y, z, x + y, x + z, y + z, x + y + z}
    if w in possible_weights:
        print('yes')
    else:
        print('no')



