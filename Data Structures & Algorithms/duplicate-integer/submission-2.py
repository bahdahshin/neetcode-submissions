class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        hashmap = {}

        for i, v in enumerate(nums):

            if v in hashmap:
                return True
            else:
                hashmap[v] = None

        return False