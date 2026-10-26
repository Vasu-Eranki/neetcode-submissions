class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        subset = []
        def recursiveSolution(start_idx:int,budget:int):
            nonlocal results,subset
            if start_idx>=len(nums):
                return
            if budget<0:
                return
            elif budget==0:
                results.append(subset.copy())
                return
            subset.append(nums[start_idx])
            recursiveSolution(start_idx,budget-nums[start_idx])
            subset.pop()
            recursiveSolution(start_idx+1,budget)
            return
        recursiveSolution(0,target)
        return results