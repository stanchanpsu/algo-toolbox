'''
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/

Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
'''

class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # If the duplicates don't have to be found, just check if the hashet length of the array is the same as the length of the array:
        return len(set(nums)) != len(nums)

        # If the duplicates have to be found use a hashtable (dict)