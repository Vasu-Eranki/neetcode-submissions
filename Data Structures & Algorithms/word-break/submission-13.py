class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [True]+[False]*n
        for idx in range(0,n,1):
            substring = s[idx:]
            for word in wordDict:
                if substring.startswith(word):
                    dp[idx+len(word)] = dp[idx+len(word)] or dp[idx]
        return dp[n]
        