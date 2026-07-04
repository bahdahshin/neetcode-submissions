class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, v in enumerate(nums):
            c = target - v
            if c not in h:
                h[v] = i
            else:
                return [h[c], i]
