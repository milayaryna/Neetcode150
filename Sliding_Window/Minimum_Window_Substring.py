# Minimum Window Substring

'''
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 
Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ''
        
        need, match, l, start, windowLen = Counter(t), 0, 0, 0, len(s) + 1
        
        for r, ch in enumerate(s):
            # keep a running count of every matching instance of a character.
            if ch in need:
                need[ch] -= 1
                match += need[ch] == 0

            # when match all the characters, shrik the window from the beginning
            while match == len(need):
                if windowLen > r - l + 1:
                    start, windowLen = l, r - l + 1
                
                # stop the shrinking process when remove a matched character from the sliding window.
                removeCh = s[l]
                l += 1 
                if removeCh in need:
                    match -= need[removeCh] == 0
                    need[removeCh] += 1

        return s[start:start + windowLen] if windowLen <= len(s) else ''
