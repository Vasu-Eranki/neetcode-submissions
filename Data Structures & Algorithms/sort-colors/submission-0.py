class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = {0:0,1:0,2:0}
        for x in nums:
            colors[x] = colors.get(x,0)+1
        index = 0
        for key,value in colors.items():
            nums[index:index+value] = [key]*value
            index = index+value
        