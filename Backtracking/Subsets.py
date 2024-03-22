# Subsets

'''
Given an integer array nums of unique elements, return all possible 
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 
Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                ans.append(subset.copy())
                return

            # 按照次序，決定要不要選入該數字
            # 選 decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            # 不選 decision not to include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return ans
