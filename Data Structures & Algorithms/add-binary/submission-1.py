class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a)>len(b):
            difference = len(a)-len(b)
            padding = '0'*difference
            b = padding+b
        else:
            difference = len(b)-len(a)
            padding = '0'*difference
            a = padding+a
        carrybit = 0
        result = ""
        for index in range(len(a)-1,-1,-1):
            digit1 = int(a[index])
            digit2 = int(b[index])
            totalsum = (digit1+digit2+carrybit)
            carrybit = totalsum//2
            result = str(totalsum%2)+result
        if carrybit:
            result = '1'+result
        return result