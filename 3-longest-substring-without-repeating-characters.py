
"""
Given a string s, find the length of the longest 
substring
 without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
"""

# Clever solution

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        sub = ''
        for char in s:
            if char not in sub:
                sub += char
                ans = max(ans, len(sub))
            else:
                cut = sub.index(char)
                # shift the window along by the index of the current character
                # that was found in the substring
                sub = sub[cut+1:] + char
        return ans


# My solution

"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialise Array to collect substrings
        substrings = ['']
        # Set currently checking substring with index
        index = 0
        # Record current start of the substring index
        substring_start_index = 0
        # Setup i to loop through string
        i = 0
        while i < len(s):
            char = s[i]
            # Check if character in the index
            if(char not in substrings[index]):
                substrings[index] += char
                i = i + 1
            else:
                # if it is, move the substring start + 1, and set i to that
                substring_start_index = substring_start_index + 1
                i = substring_start_index
                # Append a new string to the start index
                substrings.append(s[substring_start_index-1])
                index += 1
        # choose the longest substring and return its length
        return len(max(substrings, key=len))
"""