class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSum = [0]
        for x in nums:
            prefixSum.append(x+prefixSum[-1])

        for idx in range(0,len(nums)):
            leftSum = prefixSum[idx]
            rightSum = prefixSum[len(nums)]-prefixSum[idx+1]
            if(leftSum==rightSum):
                return idx
        return -1