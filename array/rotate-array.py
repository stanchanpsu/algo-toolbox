'''
https://leetcode.com/problems/rotate-array/description/

Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

Hint:
Could you do it in-place with O(1) extra space?

Related problem: Reverse Words in a String II
'''

class Solution:

    # how to reverse an array in n/2 time
    def reverse(self, array, begin, end):
        end -= 1
        while begin < end:
            array[begin], array[end] = array[end], array[begin]
            begin += 1
            end -= 1

    
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        # account for k > len(nums)
        k %= len(nums)

        # reverse entire array
        self.reverse(nums, 0, len(nums))

        # reverse subarray before rotation point
        self.reverse(nums, 0, k)

        # reverse subarray after rotation point
        self.reverse(nums, k, len(nums))