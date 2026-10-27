class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while(l<r):
            m = l + (r-l)//2
            if(nums[m]>nums[r]):
                # pivot is on the left side
                l = m+1
            else:
                #pivot is on the right side
                r = m
        pivot = l 
        l,r = 0,len(nums)-1 
        if target >= nums[pivot] and target <= nums[r]:
            l = pivot
        else:
            r = pivot - 1
        while(l<=r):
            mid = l + (r-l)//2
            if(nums[mid]==target):
                return mid
            elif nums[mid]>target:
                r = mid -1 
            else:
                l = mid+1
        return -1
        