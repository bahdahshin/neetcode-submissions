class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for _, val in enumerate(nums):
            if val in hashmap:
                return True
            else:
                hashmap[val] = None
        return False