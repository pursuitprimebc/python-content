''' question - Check if the array is sorted
Given an array nums which is rotated. You have to find out if the given array is sorted and rotated.

An array is considered sorted and rotated if:

There exists a non-decreasing sorted array A.
After rotating A by some k positions (possibly k=0), we obtain the given array nums.
Rotation means some suffix of A is moved to the front, keeping the relative order of elements.
Duplicates are allowed in the array.

Note:
If A is the original sorted array and it is rotated right by k positions, the resulting array B satisfies: B[(i+k)modA.length]=A[i] for every valid index i.
1 2 3 4 5 is a sorted array and 2 3 4 5 1 is also a sorted array but after 4 rotations.

Function Declaration
Function Name
check - This function checks whether a given array nums is a non-decreasing sorted array that has been rotated any number of times (including zero rotations).

Parameters 
nums : A reference to a vector of integers representing the array.

Return Value
Returns true if the array nums can be obtained by rotating a non-decreasing sorted array.
Returns false otherwise.

Input Format
The first line contains an integer N — the size of the array.
The second line contains N space-separated integers — the elements of the array nums.

Output Format
true if the array is sorted in non-decreasing order and then rotated any number of times (including zero).
false otherwise.
'''



class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        breaks = 0
        n = len(nums)
        
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                breaks += 1
                
        return breaks <= 1
        