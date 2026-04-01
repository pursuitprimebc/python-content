''' question - Longest subarray with a given sum
You are given an array of integers nums with length n and an integer k. Your task is to determine the length of the longest continuous 
sub-array whose elements sum up exactly to k. If there is no such sub-array, return 0.
Function Declaration
Function Name
longestSubarraySum - This function computes the length of the longest continuous sub-array whose sum is exactly equal to k.

Parameters
arr : A vector of integers of length n, representing the array.k : An integer representing the required target sum.
Return Value
Returns a single integer — the maximum length of any continuous sub-array whose sum equals k. If no such sub-array exists, the function returns 0.
The input and output formats given below are only if you want to test using custom inputs.
 
Input Format
The first line of input will contain a single integer T, denoting the number of test cases.

Each test case consists of multiple lines of input.

The first line of each test case contains two space-separated integers n and k — the length of the array and the required sum respectively.
The next line contains n space-separated integers, representing the array nums.
Output Format
For each test case, output on a new line a single integer — the length of the longest continuous subarray whose sum is exactly k. If no such subarray exists, output 0.
'''


class Solution:
    def longestSubarraySum(self, nums, k):
        # write your code here
        prefix_map = {0: -1}
        current_sum = 0
        max_length = 0
        
        for i in range(len(nums)):
            current_sum += nums[i]
            target = current_sum - k
            if target in prefix_map:
                max_length = max(max_length, i - prefix_map[target])
            
            if current_sum not in prefix_map:
                prefix_map[current_sum] = i
                
        return max_length


