class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        is_positive = False
        is_negative = False

        previous_value = nums[0]
        for i in range(1, len(nums)):
            if nums[i] - previous_value > 0:
                is_positive = True
            if nums[i] - previous_value < 0:
                is_negative = True
            previous_value = nums[i]
        
        if is_positive and is_negative:
            return False
        else:
            return True
