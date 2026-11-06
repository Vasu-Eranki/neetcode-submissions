class Solution:

    def __init__(self, w: List[int]):
        self.w = w 
        self.prefixSum = [0]
        cumSum = sum(w)
        for w_ in w:
            self.prefixSum.append((self.prefixSum[-1]+w_))
        self.prefixSum.pop(0)
        self.prefixSum = [i/cumSum for i in self.prefixSum]
    def pickIndex(self) -> int:
        random_number = random.random()
        left = 0 
        right = len(self.w)-1
        while(left<=right):
            mid = left+(right-left)//2
            if self.prefixSum[mid]==random_number:
                return self.w[mid]
            if self.prefixSum[mid]<random_number:
                left = mid+1
            else:
                right  = mid-1

        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()