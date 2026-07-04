class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()

        for kk, vv in enumerate(nums):
            if vv in s:
                return True
            else:
                s.add(vv)
        return False