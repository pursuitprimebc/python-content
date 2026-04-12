'''Move all the zeros to the last
You are given an integer array
nums. Your task is to shift all the zeroes to the end of the array, while keeping the relative order of the non-zero elements unchanged.

Important: The transformation must be done in-place without using an extra array.

Function Declaration
Function Name
moveZeroes — This function shifts all zeroes in the array to the end, while preserving the order of the remaining elements.

Parameters
nums: A reference to a array of integers.

The array contains both zero and non-zero integers.
You must modify the array directly (in-place), without allocating another array.
Return Value
This function returns void. The rearranged elements must be stored directly inside the original nums array.

The input and output formats provided below are only for testing with custom inputs.

Input Format
The first line contains a single integer T — the number of test cases.
For each test case:
The first line contains an integer N — the length of the array.
The second line contains N space-separated integers representing the array.
Output Format
For each test case, print the modified array after all zeroes have been moved to the end.
If the array has only non-zero numbers, print it unchanged.
'''

class Solution:
    def moveZeroes(self, nums):
        # write your code here
        new_pos = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[new_pos], nums[i] = nums[i], nums[new_pos]
                new_pos += 1
        return new_pos

