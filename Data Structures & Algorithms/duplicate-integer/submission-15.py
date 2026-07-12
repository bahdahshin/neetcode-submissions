class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for k, v in enumerate(nums):
            if v not in s:
                s.add(v)
            else:
                return True
        return False