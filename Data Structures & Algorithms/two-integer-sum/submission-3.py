class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for key, val in enumerate(nums):
            complement = target - val

            if complement in hashmap:
                return [hashmap[complement], key]
            else:
                hashmap[val] = key