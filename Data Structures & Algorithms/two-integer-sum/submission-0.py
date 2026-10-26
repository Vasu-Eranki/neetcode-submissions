class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookbackwards = {}
        for idx, x in enumerate(nums):
            if x in lookbackwards:
                return [lookbackwards[x],idx]
            else:
                lookbackwards[target-x] = idx
        