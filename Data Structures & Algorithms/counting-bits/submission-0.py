class Solution:
    def getBits(self,n)->int:
        results = 0
        while(n):
            results+=n%2
            n = n>>1
        return results
    def countBits(self, n: int) -> List[int]:
        values = [self.getBits(i) for i in range(0,n+1)]
        print(values)
        return values
        