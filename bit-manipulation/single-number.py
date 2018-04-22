'''
https://leetcode.com/problems/single-number/description/

Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0

        # XOR of the whole list will cause all the duplicates to cancel out and leave the single outlier
        for num in nums:
            a ^= num
        return a