class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        hashmap = {0:0}
        def dfs(amount):
            if amount==0:
                return 0
            if amount in hashmap:
                return hashmap[amount]
            number_of_coins = float('inf')
            for coin in coins:
                if amount-coin>=0:
                    number_of_coins = min(number_of_coins,1+dfs(amount-coin))
            hashmap[amount] = number_of_coins
            return number_of_coins
        dfs(amount)
        return hashmap[amount] if hashmap[amount]!=float('inf') else -1
        