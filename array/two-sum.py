'''
https://leetcode.com/problems/two-sum/description/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        s = {}

        # Put all the numbers in a dict where the values are the index
        for i in range(len(nums)):
            s[nums[i]] = i

        # Return the pair checking to make sure we dont use the same number added to itself
        for i in range(len(nums)):
            c = target-nums[i]
            if c in s and s[c] != i:
                return [i, s[c]]