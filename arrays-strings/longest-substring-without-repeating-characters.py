class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l = 0
        longest_substring = set()
        longest = 0 
        for r in range(n):
            while s[r] in longest_substring:
                longest_substring.remove(s[l])
                l += 1
            
            w = (r - l) + 1
            longest = max(longest, w)
            longest_substring.add(s[r])
        return longest