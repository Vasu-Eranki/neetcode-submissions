class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        elif n==1:
            return x
        if n<0:
            x = 1/x
            n*=-1
        result = 1
        while(n):
            if(n%2):
                result*=x
            n = n>>1;
            x*=x 
        return result
                

        