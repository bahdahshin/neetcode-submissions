class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, v in enumerate(nums):
            other_v = target - v
            
            if other_v in hashmap:
                return [hashmap[other_v], i]
            else:
                hashmap[v] = i