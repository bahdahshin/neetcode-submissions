class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        l = 0
        result = 0

        for r in range(len(s)):
            if s[r] in hashmap:
                l  = max(hashmap[s[r]] + 1, l)
            hashmap[s[r]] = r
            result = max(result, r - l + 1)

        return result