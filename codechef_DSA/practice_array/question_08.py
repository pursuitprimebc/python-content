''' question -  Single number in multiple numbers
You are given a non-empty array of integers nums.
In this array, every number occurs exactly twice except for one number that occurs only once.
Your task is to find and return that unique number.

The solution must run in O(n) time complexity and use O(1) space complexity.

Function Declaration
Function Name singleNumber - Finds the one number in the array that appears exactly once while all other numbers appear twice.

Parameters
nums : A list/array of integers where every value appears exactly twice except one.
Return Value
Returns an integer —
the unique number that appears only once.
Input Format
N → number of elements in the array
Next line → N integers representing nums
Output Format
Print the single number that appears exactly once.
'''


class Solution:
    def singleNumber(self, nums):
        result = 0
        
        for num in nums:
             result ^= num
    
        return result
