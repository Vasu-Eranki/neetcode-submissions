class Solution:
    def numDecodings(self, s: str) -> int:
        hashmap = {}
        def dfs(i):
            if i==len(s):
                return 1
            elif s[i]=='0': # has a leading zero, cannot decode
                return 0
            elif i>len(s):
                return 0
            elif i in hashmap:
                return hashmap[i]
            two_letter_word = int(s[i:i+2])
            if two_letter_word<=26 and two_letter_word>=10:
                hashmap[i] = dfs(i+1)+dfs(i+2)
            else:
                hashmap[i] = dfs(i+1)
            return hashmap[i]

        
        return dfs(0)


        