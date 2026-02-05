''' QUESTION -Chef and Battery
Chef's phone has a battery level of N percent.
Each minute:
If the phone is on charging, the battery level increases by 2%.
Otherwise, the battery level decreases by 3%.

Find the minimum time in which Chef can make the battery level reach exactly 50%.
Note that the battery level should always lie in the range 0 to 100 (both included).

Input Format
The first line of input will contain a single integer T, denoting the number of test cases.
Each test case consists of single lines of input N - the current battery level of Chef's phone.

Output Format
For each test case, output on a new line the minimum time in which Chef can make the battery level reach exactly 50%.
'''



t = int(input())
for i in range(t):
    n = int(input())
    minutes = 0
    
   
    while n != 50:
        if n > 50:
            n -= 3
        else:
            n += 2
        minutes += 1
        
    print(minutes)


