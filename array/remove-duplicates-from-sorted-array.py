'''
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
'''

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return len(nums)
        l = 0
        # If new number found insert it into the l pointer position and increment l
        for i in range(1, len(nums)):
            if nums[i] != nums[l]:
                l += 1
                nums[l] = nums[i]

        # At the end of the for loop, l is the length of the new array - 1
        return l + 1