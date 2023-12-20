# Search in Rotated Sorted Array

'''
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.


Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            # At any point in the rotated arrary, one half will always be sorted.
            if nums[l] <= nums[mid]:
            # left half is sorted.
                if nums[l] <= target <= nums[mid]:
                # target in this half.
                    r = mid - 1
                else:
                    l = mid + 1

            else:
            # right half is sorted.
                if nums[mid] <= target <= nums[r]:
                # target in this half.
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
