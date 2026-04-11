'''Rotate the array
You are given an integer array 
nums. Rotate the array to the right by k positions, where k is a non-negative integer.
For example:
Given the array [10, 20, 30, 40, 50], rotating it two times to the right results in:
First rotation - [50, 10, 20, 30, 40]
Second rotation - [40, 50, 10, 20, 30]
You need to implement a solution that operates in-place and uses only O(1) additional space.
You don't need to print any values; simply edit the values of the array.

Function Declaration
Function Name
rotate - This function rotates an array to the right by k positions in-place.

Parameters
nums : An array of integers.
k : A non-negative integer representing the number of right rotations.
Return Value
This function does not return anything.
The array nums is modified in-place.
'''



def rotate(nums, k):
    n = len(nums)
    k=k%n
    if n == 0 or k==0:
        return nums
        
    nums[:] = nums[-k:] + nums[:-k] 
    return nums