class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = nums[0]
        maxSum = nums[0]
        for idx in range(1,len(nums)):
            currSum = max(currSum+nums[idx],nums[idx])
            maxSum = max(maxSum,currSum)
        return maxSum
        