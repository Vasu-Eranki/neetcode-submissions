class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        fast_pointer = len(nums)-k
        nums_copy = nums.copy() 
        slow_pointer = 0 
        while(slow_pointer<len(nums)):
            nums[slow_pointer] = nums_copy[fast_pointer%len(nums)]
            fast_pointer+=1
            slow_pointer+=1

