class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        counter = 0
        string = ""
        for i in range(len(s)):
            if s[i]=="(":
                counter+=1
            elif s[i]==")":
                if counter==0:
                    continue
                counter-=1
            string+=s[i]

        counter = 0
        result = ""
        for i in range(len(string)-1,-1,-1):
            if string[i]==")":
                counter+=1
            elif string[i]=="(":
                if counter==0:
                    continue
                counter-=1
            result=string[i]+result
        return result
        