class Solution:
    def greedy(self,nums:List[int],max_value:int)->tuple[int,int]: #length
        results = []
        cumSum = 0 
        for i in nums:
            cumSum+=i
            if(cumSum==max_value):
                results.append(cumSum)
                cumSum = 0 
            elif(cumSum>max_value):
                cumSum-=i
                results.append(cumSum)
                cumSum=i
        if(cumSum):
            results.append(cumSum)
        return len(results),max(results) # number of values,  max of the sub array
            


    def splitArray(self, nums: List[int], k: int) -> int:
        if k==1:
            return sum(nums)
        elif k==len(nums):
            return max(nums)
        left = max(nums)
        right =max_value= sum(nums)
        while(left<right):
            mid = left + (right-left)//2
            length_of_subarray,max_value_of_subarray = self.greedy(nums,mid)
            if length_of_subarray<=k:
                max_value = min(max_value,max_value_of_subarray)
                right = mid
            else:
                left = mid+1
        return max_value
        