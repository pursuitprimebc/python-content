''' QUESTION - Largest Odd Substring
You are given a string nums consisting of digits representing a large integer. Your task is to find the largest-valued odd integer (as a substring of nums) that can be obtained.

A substring is a contiguous sequence of characters within the string.

Function Declaration
Function Name findLargestOddSubstring - This function finds the largest-valued odd integer that can be obtained as a substring of the given numeric string.

Parameters
num : A string representing a large integer, consisting only of digits (0-9).
Return Value
This function prints:

The largest odd integer substring if it exists. -1 if no odd integer substring can be formed.

Constraints
1≤|num|≤10^5
The string num contains only digits 0-9
The string does not contain leading zeros
There is no limit on the size of the integer represented by the substring

Input Format
The first line contains a single string num.

Output Format
Print a single line:
The largest odd integer substring of num
Or -1 if no odd substring exists
'''


def findLargestOddSubstring(num):
    odd_num = ""
    for i in range(len(num)):
        a = (len(num)-1)-i 
        if int(num[a])%2!=0:
            odd_num = num[:a+1]
            return(odd_num)
    
    
    return('-1')
        
    
try:
    num = input().strip()
    if num:
        print(findLargestOddSubstring(num))
except EOFError:
    pass