class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        subsets = []
        def dfs(index):
            if index==len(nums):

                results.append(subsets.copy())
                return 
            subsets.append(nums[index])
            dfs(index+1)
            subsets.pop()
            dfs(index+1)
            return 
        dfs(0)
        return results
        