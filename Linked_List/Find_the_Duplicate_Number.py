# Find the Duplicate Number

'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Fast-Slow Pointers Approach (Floyd's Cycle Detection)
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]  # slow pointer moves one step at a time.
            fast = nums[nums[fast]]  # fast pointer moves two steps at a time.
            if slow == fast:
                break
            # The loop continues until both pointers meet at some point within the cycle. 
            # Note that this meeting point is not necessarily the duplicate number; it's just a point inside the cycle.

        # After identifying a meeting point inside the cycle, we reinitialize the slow pointer back to nums[0]. 
        # The fast pointer stays at the last meeting point.
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        # After identifying a meeting point inside the cycle, we reinitialize the slow pointer back to nums[0]. 
        # The fast pointer stays at the last meeting point.

        return slow
