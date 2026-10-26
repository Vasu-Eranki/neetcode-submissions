class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while(columnNumber):
            value = columnNumber%26
            if(value==0):
                result+="Z"
                break
            result+=chr(64+value)
            columnNumber = columnNumber//26
        return result[::-1]
        