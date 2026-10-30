class NumArray:

    def __init__(self, nums: List[int]):
        self.results = []
        currentSum = 0
        for x in nums:
            if self.results:
                self.results.append(self.results[-1]+x) 
            else:
                self.results=[x]
    def sumRange(self, left: int, right: int) -> int:
        prefixRight = self.results[right]
        prefixLeft = self.results[left-1] if left else 0
        return prefixRight - prefixLeft
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)