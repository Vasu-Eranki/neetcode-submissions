class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        concatenation = ""
        while(word1 and word2):
            concatenation = concatenation + word1[0] + word2[0]
            word1 = word1[1:]
            word2 = word2[1:]
        while(word1):
            concatenation+=word1[0]
            word1 = word1[1:]
        while(word2):
            concatenation+=word2[0]
            word2 = word2[1:]
        return concatenation
        
        