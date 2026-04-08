'''Remove Duplicates from Sorted Array
Chef has an integer array nums sorted in non-decreasing order.
Chef wants to remove all duplicate elements from the array in-place such that each unique element appears only once.

The relative order of the elements should remain the same.

After removing the duplicates, let the number of unique elements be K.
The first K elements of the array should contain the unique elements in their original order.
The values beyond the first K elements do not matter.
Your task is to help Chef find K and print the first K elements of the modified array.

Function Declaration
Function Name
removeDuplicates - Removes duplicate elements from a sorted array in-place.

Parameters
nums : A list/array of integers sorted in non-decreasing order.
Return Value
Returns an integer K — the number of unique elements.
The first K positions of nums must contain these unique values.
'''


def remove_duplicates(nums):
    if not nums:
        return 0
        
    unique_ptr = 0
        
   
    for i in range(len(nums) - 1, 0, -1):
        if nums[i] == nums[i - 1]:
            nums.pop(i) 
            
    return len(nums)
    
try:
    n = int(input())
    nums = list(map(int, input().split())) 
    k = remove_duplicates(nums)
    print(k)    
    print(*nums)
except EOFError:
    pass