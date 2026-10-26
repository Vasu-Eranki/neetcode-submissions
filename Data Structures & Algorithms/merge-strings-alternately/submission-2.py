class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pointer1 = 0 
        pointer2 = 0 
        result = []
        while(pointer1<len(word1) and pointer2 < len(word2)):
            result.append(word1[pointer1])
            result.append(word2[pointer2])
            pointer1+=1
            pointer2+=1
        while(pointer1<len(word1)):
            result.append(word1[pointer1])
            pointer1+=1
        while(pointer2<len(word2)):
            result.append(word2[pointer2])
            pointer2+=1
        return "".join(result)
        