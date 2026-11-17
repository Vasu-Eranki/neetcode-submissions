class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        subsets = []
        def dfs(index,target):
            if target<0:
                return 
            if target==0:
                results.append(subsets.copy())
                return
            if index==len(nums):
                return 
            value = nums[index]
            subsets.append(value)
            dfs(index,target-value)
            subsets.pop()
            dfs(index+1,target)
            return 
        dfs(0,target)
        return results
            
        