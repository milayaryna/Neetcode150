# Combination Sum II

'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.


Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
'''

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(cur, pos, target):
            if target == 0:  # If the target is reached, add the current combination to the result
                res.append(cur.copy())
                return
            if target <= 0:
                return

            prev = -1  # Variable to keep track of the previous candidate to avoid duplicates

            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue

                cur.append(candidates[i])
                backtrack(cur, i + 1, target - candidates[i])
                cur.pop()
                prev = candidates[i]
            
        backtrack([], 0, target)
        return res
