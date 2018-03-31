'''
https://leetcode.com/problems/valid-parentheses/description/

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        p = {'(':')', '{':'}', '[':']'}
        for c in s:
            if c in p:
                stack.append(c)
            else:
                if not stack or p[stack.pop()] != c:
                    return False
        return not stack