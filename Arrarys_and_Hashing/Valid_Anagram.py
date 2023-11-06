# Arrays & Hashing
# Valid Anagram

'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)  # sorted_s = ['a', 'a', 'a', 'g', 'm', 'n', 'r']
        sorted_t = sorted(t)  # sorted_t = ['a', 'a', 'a', 'g', 'm', 'n', 'r']
        return sorted_s == sorted_t
