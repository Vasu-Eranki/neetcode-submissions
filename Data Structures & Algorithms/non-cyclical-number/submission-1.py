class Solution:
    def calculateHappy(self,n:int)->int:
        result = 0
        while(n):
            units_place = n%10
            result +=(units_place**2)
            n = n//10
        return result
    def isHappy(self, n: int) -> bool:
        hashmap = {}
        value = n
        while(True):
            value = self.calculateHappy(value)
            if(value==1):
                return True
            if(not hashmap.get(value,False)):
                hashmap[value]=True
            else:
                return False
        