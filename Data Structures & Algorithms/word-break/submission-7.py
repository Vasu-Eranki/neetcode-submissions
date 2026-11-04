class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        hashmap = {}
        def dfs(i):
            if i==len(s):
                return True
            if i in hashmap:
                return hashmap[i]
            else:
                hashmap[i] = False
                for word in wordDict:
                    substr = s[i:]
                    if substr.startswith(word):
                        hashmap[i] = dfs(i+len(word))
                        if hashmap[i]:
                            break
            return hashmap[i]
        dfs(0)
        return hashmap[0]
