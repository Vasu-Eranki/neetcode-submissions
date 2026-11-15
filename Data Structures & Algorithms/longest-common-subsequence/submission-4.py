class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        x = text1
        y = text2
        if len(text1)>len(text2):
            x = text2 
            y = text1 
        # x is the smaller string 
        # y is the longer string
        # we will try to match each character in x with y
        memo = {}
        def dp(index_x:int,index_y:int)->int:

            if index_x==len(x):
                return 0 # we have reached the end of our shorter string, can no longer mathc
            if index_y==len(y): # we have reached the end of our long, no more characters to match
                return 0
            if (index_x,index_y) in memo:
                return memo[(index_x,index_y)]
            character = x[index_x]
            current_character_at_y = y[index_y]
            if character==current_character_at_y:
                max_substring = 1 + dp(index_x+1,index_y+1)
            else:
                max_substring = max(dp(index_x+1,index_y),dp(index_x,index_y+1))
            memo[(index_x,index_y)] = max_substring
            return max_substring
        max_substring = 0
        return dp(0,0)