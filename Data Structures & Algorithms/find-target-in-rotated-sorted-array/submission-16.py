class Solution:
    def findPivot(self,nums:List[int])->tuple[int,int]:
        left = 0 
        right = len(nums)-1
        while(left<right):
            mid = left + (right-left)//2
            if nums[mid]<nums[right]:
                right = mid
            else:
                left = mid+1
        return left
    def binarySearch(self,nums:List[int],target:int,left:int,right:int)->int:
        while(left<=right):
            mid = left + (right-left)//2
            print(left,right,nums[mid])
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right = mid-1
            else:
                left = mid+1
        return -1
    def search(self, nums: List[int], target: int) -> int:
        pivot = self.findPivot(nums)
        left,right = 0, len(nums)-1
        if target<=nums[right] and nums[pivot]<=target:
            left = pivot
        else:
            right = pivot-1
        index = self.binarySearch(nums,target,left,right)
        return index
        