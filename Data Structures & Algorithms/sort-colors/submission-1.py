class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = {}
        for x in nums:
            colors[x] = colors.get(x,0)+1
        colors = list(colors.items())
        colors.sort(key=lambda x:x[0])
        colors = dict(list(colors))
        index = 0
        for key,value in colors.items():
            nums[index:index+value] = [key]*value
            index = index+value
        