# Longest Repeating Character Replacement

'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 
Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        MaxSameChar = 0

        for right in range(len(s)):
            # count how many times the character has appeard.
            count[s[right]] = 1 + count.get(s[right], 0) # if can't get s[r], return 0.
            MaxSameChar = max(MaxSameChar, count[s[right]])

            # can't replace the diference with character, move the left pointer forward.
            if (right - left + 1) - MaxSameChar > k:
                count[s[left]] -= 1
                left += 1
        return (right - left + 1)
