'''
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/674/


Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
'''


class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        answer = []
        n1 = {}

        # Make the first list into a dict
        for n in nums1:
            if n in n1:
                n1[n] += 1
            else:
                n1[n] = 1

        # For each number in the second list, if it's in the dict, put it in the answer array and subtract the count in the dict
        for n in nums2:
            if n in n1:
                if n1[n] > 0:
                    n1[n] -= 1
                    answer.append(n)
        return answer