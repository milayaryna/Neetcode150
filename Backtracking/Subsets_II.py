# Subsets II

'''
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
'''

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        nums.sort()  # To ensure that duplicate elements appear next to each other.

        def dfs(i):
            if i == len(nums):
                result.append(subset.copy())
                return

            # 選
            subset.append(nums[i])
            dfs(i + 1)

            # 不選
            subset.pop()
            # Skip over consecutive duplicates to avoid generating duplicate subsets
            while (i + 1) < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i + 1)

        dfs(0)
        return result
