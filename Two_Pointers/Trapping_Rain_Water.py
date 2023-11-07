# Trapping Rain Water

'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.


Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
'''

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l = 0
        r = len(height) - 1
        res = 0

        LeftMax = height[l]
        RightMax = height[r]

        # the highest bar is the center.
        while l < r:
            # water collected from the left hand side.
            if LeftMax < RightMax:
                l += 1
                LeftMax = max(LeftMax, height[l])
                res += LeftMax - height[l]
            # water collected from the right hand side.
            else:
                r -= 1
                RightMax = max(RightMax, height[r])
                res += RightMax - height[r]
        return res
