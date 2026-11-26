class Solution:
    def cumSum(self,nums:List[int],maxValue:int)->int:
        # maxValue tells how much can be in one segment
        # returns the number of segments 
        cumulativeSum = 0 
        segments = 0 
        for x in nums:
            cumulativeSum+=x
            if cumulativeSum==maxValue:
                cumulativeSum=0
                segments+=1
            elif cumulativeSum>maxValue:
                cumulativeSum=x
                segments+=1
        segments+=bool(cumulativeSum)
        return segments
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums) 
        while(left<right):
            mid = left + (right-left)//2
            number_of_segments = self.cumSum(nums,mid)
            if number_of_segments<=k:
                right = mid
            else:
                left = mid+1

        return left
        

        