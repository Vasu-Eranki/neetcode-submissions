class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(amount):
            if amount==0:
                return 0
            if amount in memo:
                return memo[amount]
            total_ways_to_make_it = float('inf')
            for coin in coins:
                if (amount-coin)>=0:
                    value=dp(amount-coin)
                    if value!=float('inf'):
                        total_ways_to_make_it = min(1+value,total_ways_to_make_it)
            memo[amount]=total_ways_to_make_it
            return total_ways_to_make_it
        value= dp(amount)
        return value if value!=float('inf') else -1

        