# Largest Rectangle in Histogram

'''
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:
Input: heights = [2,4]
Output: 4
'''

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (index, height) = (stackInd, stackH)
        maxArea = 0

        heights = heights + [-1]
        # add -1 to have an additional iteration

        for h in heights:
            step = 0
            while stack and stack[-1][1] >= h:
                stackInd, stackH = stack.pop()
                step += stackInd
                maxArea = max(maxArea, step*stackH)
            stack.append((step+1, h))

        return maxArea
