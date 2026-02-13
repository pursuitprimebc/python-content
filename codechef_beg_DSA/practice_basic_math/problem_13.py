''' QUESTION - GCD and LCM
Two integers A and B are the inputs. Write a program to find GCD and LCM of A and B.

Input Format
The first line contains an integer T, total number of testcases. Then follow T lines, each line contains an integer A and B.

Output Format
Display the GCD and LCM of A and B separated by space respectively. The answer for each test case must be displayed in a new line.
'''


def find_gcd(a,b):
    while b:
        a ,b = b , a%b 
    return a 

def find_lcm(a,b):
    if a==0 or b==0:
        l = 0
    else:
        # formula for LCM is (a*b)/GCD 
        l = abs(a*b)//find_gcd(a,b)
    return l
    
    
t = int(input())
while t > 0:
    a, b = map(int, input().split())
    t -= 1
    print(find_gcd(a,b),find_lcm(a,b))
    
    