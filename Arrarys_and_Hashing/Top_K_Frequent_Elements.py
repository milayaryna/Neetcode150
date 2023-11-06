# Top K Frequent Elements

'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}  # value:count
        freq = [[] for i in range(len(nums) + 1)]
        # list of count from 0 to (len(nums) + 1), will fill in with nums later.

        for n in nums:
            count[n] = 1 + count.get(n, 0)  # It returns the default value 0 if the key is missing.
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
        # catch the k most frequent elements.
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
