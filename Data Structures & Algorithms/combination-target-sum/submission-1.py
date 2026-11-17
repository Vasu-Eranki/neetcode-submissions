class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = set()
        subsets = []
        def dfs(index,target):
            if target<0:
                return 
            if target==0:
                results.add(tuple(subsets.copy()))
            if index==len(nums):
                return 
            value = nums[index]
            subsets.append(value)
            dfs(index,target-value)
            subsets.pop()
            dfs(index+1,target)
            return 
        for i in range(0,len(nums)):
            dfs(i,target)
        return[list(i) for i in results]
            
        