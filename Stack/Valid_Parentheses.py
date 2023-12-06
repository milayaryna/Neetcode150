# Valid Parentheses

'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
'''

class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")":"(", "]":"[", "}":"{"}
        stack = []

        for i in s:
            if i not in Map:
                stack.append(i)
                continue
            if not stack or stack[-1] != Map[i]:
            # i is close bracket, but no open bracket in stack.
            # the last open bracket can not be closed by the same type of bracket.
                return False
            if stack[-1] == Map[i]:
                stack.pop()
        
        return not stack
        # return true if there is no open brackrt in stack.
