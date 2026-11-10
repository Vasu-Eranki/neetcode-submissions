class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        if len(target)>len(words[0]): # more characters than what we have
            return 0
        index_hashmap = [{} for _ in range(len(words[0]))]
        for i in range(len(words)):
            for j in range(len(words[0])):
                hashmap = index_hashmap[j]
                character = words[i][j]
                hashmap[character]= hashmap.get(character,0)+1
        n = len(target)
        dp = [1]+[0]*n
        for i in range(0,len(index_hashmap)):
            hashmap = index_hashmap[i]
            for j in range(min(i+1,n),0,-1):
                character = target[j-1]
                dp[j] = (dp[j]+dp[j-1]*hashmap.get(character,0))%(10**9+7)
        return dp[-1]
            