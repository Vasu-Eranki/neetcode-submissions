class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow_pointer= 0
        for fast_pointer in range(len(nums)):
            if(nums[fast_pointer]!=val):
                nums[slow_pointer]=nums[fast_pointer]
                slow_pointer+=1
        return slow_pointer

        