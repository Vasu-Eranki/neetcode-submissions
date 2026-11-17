class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        def backtracking(start,stop):
            if start==stop:
                results.append(nums.copy()) # only one way to permute an element of length 
                return
            for idx in range(start,len(nums)):
                nums[idx],nums[start] = nums[start],nums[idx] # swap them 
                backtracking(start+1,stop)
                nums[idx],nums[start] = nums[start],nums[idx] # swap them 
            return
        backtracking(0,len(nums))
        return results
        