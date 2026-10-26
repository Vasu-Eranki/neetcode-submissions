class Solution:
    def climbStairs(self, n: int) -> int:
        results = [0,1,2]
        if(n<=2):
            return results[n]
        for i in range(2,n):
            value = results[-1]+results[-2]
            results.append(value)
        return results[-1]
        