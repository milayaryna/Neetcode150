# Permutation in String

'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 
Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = {c: 0 for c in string.ascii_lowercase}
        window = {c: 0 for c in string.ascii_lowercase}
        n = len(s1)
        for c in s1:
            target[c] += 1
        for c in s2[:n]:
            window[c] += 1
        for i in range(n, len(s2)):
            if window == target:
                return True
	    # sliding window
            window[s2[i-n]] -= 1
            window[s2[i]] += 1
        return window == target
