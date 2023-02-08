"""
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
"""

# Expanding out from the center of a palendrome

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if(len(s) == 1):
            return s
        longest = 0
        result = ''
        for i in range(len(s)):
            # check for odd palendromes, expanding out from the center
            left, right = i, i
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                if(len(s[left:right+1]) > longest):
                    result = s[left:right+1]
                    longest = right - left + 1
                left -= 1
                right += 1
            # check for evenly centered palendromes,
            left, right = i, i+1
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                if(len(s[left:right+1]) > longest): # if longest, update result and longest
                    result = s[left:right+1]
                    longest = right - left + 1
                left -= 1
                right += 1
        return result

# Brute Force
# O(n^3) time | O(1) space
"""
class Solution:

    def isPalindrome(self, s: str) -> str:
        backwards = s[::-1]
        return s == backwards

    def longestPalindrome(self, s: str) -> str:
        if(len(s) == 1):
            return s
        sub = ''
        longest_sub = ''
        for i in range(len(s)):
            for j in range(1,len(s)+1):
                sub = s[i:j]
                if(self.isPalindrome(sub)):
                    longest_sub = max([sub, longest_sub], key=len)
        return longest_sub
"""