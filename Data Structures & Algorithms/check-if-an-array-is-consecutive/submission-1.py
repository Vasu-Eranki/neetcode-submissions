class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        min_value = min(nums)
        max_value = max(nums)
        return True if (min_value+len(nums)-1)==max_value else False
