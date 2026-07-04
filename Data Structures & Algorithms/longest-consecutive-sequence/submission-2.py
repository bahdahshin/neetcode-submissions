class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        from collections import defaultdict
        mp = defaultdict(int)
        res = 0

        for num in nums:
            if not mp[num]:
                mp[num] = mp[num - 1] + 1 + mp[num + 1]
                mp[num - mp[num - 1]] = mp[num] # left most neighbor
                mp[num + mp[num + 1]] = mp[num] # right most neighbor
                res = max(res, mp[num])

        return res