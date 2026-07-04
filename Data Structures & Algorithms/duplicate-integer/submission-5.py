"""
if array item is more than once True, else False
"""
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        
        for _, v in enumerate(nums):
            if v in hashmap:
                return True
            else:
                hashmap[v] = None
            
        return False