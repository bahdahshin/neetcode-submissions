class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        for i, _ in enumerate(nums):
            total = 1
            for j, _ in enumerate(nums):
                if i != j:
                    total = total * nums[j]
            result.append(total)

        return result