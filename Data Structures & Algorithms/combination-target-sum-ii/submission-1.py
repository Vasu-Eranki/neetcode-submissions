class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = [i for i in candidates if i<=target] # removing numbers that are greater than target. minimizes DP search space 
        candidates.sort()
        results = []
        subsets = []
        def dp(index,target):
            if target<0:
                return
            elif target==0:
                results.append(subsets.copy())
                return 
            elif index>=len(candidates):
                return 
            value = candidates[index]
            newTarget = target-value 
            subsets.append(candidates[index])
            dp(index+1,newTarget)
            while(index<len(candidates) and candidates[index]==value):
                index+=1
            subsets.pop()
            dp(index,target)
            return 
        dp(0,target)
        return results