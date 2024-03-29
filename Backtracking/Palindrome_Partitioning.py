# Palindrome Partitioning

'''
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]
'''

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result, part = [], []

        def dfs(i):
            if i >= len(s):
                result.append(part.copy())
                return
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    part.append(s[i:j+1])
                    # Recursively call dfs with the next index (j + 1) to continue partitioning.
                    dfs(j+1)
                    part.pop()

        dfs(0)
        return result

    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
