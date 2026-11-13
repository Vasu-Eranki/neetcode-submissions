class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dfs(index):
            if index>=len(nums):
                return 0
            if index in memo:
                return memo[index]
            LIS =1
            value = nums[index]
            for i in range(index+1,len(nums)):
                if nums[i]>value:
                    LIS = max(LIS,1+dfs(i))
            memo[index] = LIS
            return LIS
        return max(dfs(i) for i in range(0,len(nums)))