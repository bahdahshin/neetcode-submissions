class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for k, v in enumerate(nums):
            compliment = target - v
            if compliment in s:
                return [s[compliment], k]
            else:
                s[v] = k