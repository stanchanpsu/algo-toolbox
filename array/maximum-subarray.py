'''
https://leetcode.com/problems/maximum-subarray/description/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        running = nums[0]
        max_sum = nums[0]
        
        for num in nums[1:]:
            running = running + num if running > 0 else num
            max_sum = running if running > max_sum else max_sum
        return max_sum