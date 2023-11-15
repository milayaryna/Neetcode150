# Sliding Window Maximum

'''
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.


Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 
Example 2:
Input: nums = [1], k = 1
Output: [1]
'''

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()  # list-like container with fast appends and pops on either end, to maintain indices of potentially maximum elements
        l = r = 0  # two pointers of the sliding window
        
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]: # nums[q[-1]] is the current maximum
                q.pop()
            q.append(r)  # append the new-current maximum

            # remove left value since it's no longer relevant for the current window.
            if l > q[0]:
                q.popleft()

            # if the current window size is equal to or larger than k, append the maximum element of the current window.
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output
