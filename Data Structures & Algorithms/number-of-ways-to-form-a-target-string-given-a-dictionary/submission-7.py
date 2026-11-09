class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        width = len(words[0]); size = len(target)
        counts = [[0]*26 for _ in range(width)]
        for word in words:
            for col,c in enumerate(word): counts[col][ord(c)-97] += 1
        dp = [1]+[0]*size
        for col in range(width):
            for j in range(min(col+1,size),0,-1):
                dp[j] = (dp[j]+dp[j-1]*counts[col][ord(target[j-1])-97])%1000000007
        return dp[size]
