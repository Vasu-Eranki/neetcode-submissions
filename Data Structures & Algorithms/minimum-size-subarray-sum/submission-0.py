class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cumSum =0 
        left_pointer = 0 
        min_len = float('inf')
        for i in range(0,len(nums)):
            cumSum+=nums[i]
            if cumSum>=target:
                while(cumSum>=target):
                    min_len = min(i-left_pointer+1,min_len)
                    value = nums[left_pointer]
                    cumSum-=value
                    left_pointer+=1
        return min_len if min_len!=float('inf') else 0 


        