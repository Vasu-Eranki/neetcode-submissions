class NumArray:

    def __init__(self, nums: List[int]):
        self.results = [0]
        currentSum = 0
        for x in nums:
            self.results.append(self.results[-1]+x) 
        self.results.pop(0)
    def sumRange(self, left: int, right: int) -> int:
        prefixRight = self.results[right]
        prefixLeft = self.results[left-1] if left else 0
        return prefixRight - prefixLeft
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)