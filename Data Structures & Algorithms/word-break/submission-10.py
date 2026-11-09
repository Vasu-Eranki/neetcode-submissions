class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def dp(index):
            if index==len(s):
                return True
            if index in memo:
                return memo[index]
            else:
                substring = s[index:]
                result = False
                for word in wordDict:
                    if substring.startswith(word):
                        result = result or dp(index+len(word))
                memo[index]=result
            return result
        return dp(0)
        