# Kth Largest Element in an Array

'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 
Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
'''

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        
        for num in nums[k:]:  # For each of the remaining elements in nums:
            if num > heap[0]:  # If the element is larger than the smallest element in the heap.
                heapq.heappop(heap)  # Remove the top element from the heap.
                heapq.heappush(heap, num)  # Insert the current element into the heap.
        
        return heap[0]
