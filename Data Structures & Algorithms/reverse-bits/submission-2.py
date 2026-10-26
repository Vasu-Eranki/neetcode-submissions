class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result+=(n%2)
            n//=2
            result*=2
        return result//2
        