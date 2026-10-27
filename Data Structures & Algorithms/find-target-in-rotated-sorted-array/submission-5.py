class Solution:
    def findPivot(self,nums:List[int])->int:
        left = 0 
        right = len(nums)-1
        while(left<right):
            mid = left + (right-left)//2
            if(nums[mid]>nums[right]):
                left = mid+1
            else:
                right = mid
        return left
    def search(self, nums: List[int], target: int) -> int:
        pivotIdx = self.findPivot(nums)
        l, r = 0, len(nums) - 1

        if target >= nums[pivotIdx] and target <= nums[r]:
            l = pivotIdx
        else:
            r = pivotIdx - 1
        while(l<=r):
            mid = l + (r-l)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                r = mid-1 
            else:
                l = mid+1
        return -1
        


        