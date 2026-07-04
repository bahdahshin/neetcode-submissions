class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for _, v in enumerate(numSet):
            if (v - 1) not in numSet:
                length = 1
                while (v + length) in numSet:
                    length += 1
                longest = max(length, longest)

        return longest