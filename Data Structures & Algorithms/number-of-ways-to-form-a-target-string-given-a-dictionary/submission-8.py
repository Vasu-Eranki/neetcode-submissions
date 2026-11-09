class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        if len(target)>len(words[0]):
            return 0
        character_frequency = [{} for _ in range(len(words[0]))]
        for i in range(len(words[0])):
            hashmap = character_frequency[i]
            words_list = [x[i] for x in words]
            for character in words_list:
                hashmap[character] = hashmap.get(character,0)+1
        dp = [1]+[0]*len(target)
        for i in range(len(words[0])):
            for j in range(min(i+1,len(target)),0,-1):
                character_freq_for_index= character_frequency[i]
                dp[j] = (dp[j]+dp[j-1]*character_freq_for_index.get(target[j-1],0))%(10**9+7)
        return dp[len(target)]



