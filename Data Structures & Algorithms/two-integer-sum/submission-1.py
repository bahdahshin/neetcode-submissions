class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}

        for i, v in enumerate(nums):
            number = target - v

            if number in hashmap:
                return [hashmap[number], i]
            else:
                hashmap[v] = i
        