class Solution:
    def climbStairs(self, n: int) -> int:
        results = [0,1,2]
        if(n<=2):
            return results[n]
        for i in range(2,n):
            results.append(results[-1]+results[-2])
        return results[-1]
        