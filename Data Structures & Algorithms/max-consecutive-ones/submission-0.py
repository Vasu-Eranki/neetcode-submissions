class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_value = 0
        max_value = 0
        for i in range(len(nums)):
            if nums[i]==1:
                current_value +=1
                max_value = max(current_value,max_value)
            else:
                current_value = 0
        return max_value
        