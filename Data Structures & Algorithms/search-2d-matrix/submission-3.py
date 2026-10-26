class Solution:
    def searchArray(self,nums:List[int],target:int)->bool:
        left = 0 
        right = len(nums)
        while(left<=right):
            mid = left + (right-left)//2
            if nums[mid]==target:
                return True
            elif nums[mid]>target:
                right = mid-1
            else:
                left = mid+1
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0 
        right = len(matrix)-1
        while(left<=right):
            mid = left + (right-left)//2
            if (matrix[mid][0]>target): # if start of matrix is already more than target
                right = mid-1
            elif (matrix[mid][0]<=target and matrix[mid][-1]>=target): # if target is in range
                return self.searchArray(matrix[mid],target)
            else:
                left = mid+1
        return False
        