class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        if not words:
            return 0
        lenght_of_words = len(words[0])
        length_of_target = len(target)
        index_of_hashmap = [{} for _ in range(lenght_of_words)]
        modulo_number = 10**9 + 7

        for i in range(len(words[0])):
            hashmap = index_of_hashmap[i]
            for word in words:
                hashmap[word[i]] = hashmap.get(word[i], 0) + 1
        dp = [1] + [0] * len(target)

        for i in range(0,lenght_of_words):
            for j in range(min(i+1,length_of_target), 0, -1):
                character = target[j-1]
                dp[j] = (dp[j - 1] * index_of_hashmap[i].get(character, 0) + dp[j])%modulo_number

        return dp[-1]%modulo_number
