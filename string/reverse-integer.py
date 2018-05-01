'''
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_neg = (x < 0)
        s = str(x)
        # remove neg sign
        if is_neg:
            s = s[1:]
        # reverse the string and strip leading zeros
        s = s[::-1]
        if is_neg:
            s = '-' + s
        if int(s) > 2**31-1 or int(s) < -(2**31):
            return 0
        else:
            return int(s)

