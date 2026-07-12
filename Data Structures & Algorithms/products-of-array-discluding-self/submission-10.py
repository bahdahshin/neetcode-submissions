class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1
        r = [1] * len(nums)

        for i in range(len(nums)):
            r[i]   *= prefix
            prefix *= nums[i]

        for i in reversed(range(len(nums))):
            r[i]    *= postfix
            postfix *= nums[i]
        return r
