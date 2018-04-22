'''
https://leetcode.com/explore/interview/card/top-interview-questions-easy/98/design/670/

Shuffle a set of numbers without duplicates.
'''


import random

class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.original = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.nums = self.original
        return self.nums


    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """

        # This is called the Fisher-Yates Algorithm where a random index is generated and then swapped with the current index
        for i in range(len(self.nums)):
            index = random.randrange(len(self.nums))
            self.nums[i], self.nums[index] = self.nums[index], self.nums[i]
        return self.nums