class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dp(index):
            if index>=len(nums):
                return 0 # we have reached the end
            if index in memo:
                return memo[index]
            value_here = nums[index]
            # we can either rob the next house after, 
            result = max(value_here+dp(index+2),dp(index+1))
            memo[index]=result
            return result
        return dp(0)
        