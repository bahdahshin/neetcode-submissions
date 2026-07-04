class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for kk, vv in enumerate(nums):
            c = target - vv
            if c in h:
                return [h[c], kk]
            else:
                h[vv] = kk