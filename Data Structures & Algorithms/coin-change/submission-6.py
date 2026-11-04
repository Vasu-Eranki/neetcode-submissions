class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        possible_coins = [float('inf') for _ in range(amount+1)]
        possible_coins[0] = 0 
        for i in range(0,amount+1):
            for j in range(0,len(coins)):
                if coins[j]<=i:
                    if i-coins[j]>=0:
                        possible_coins[i] = min(possible_coins[i],1+possible_coins[i-coins[j]])
        return possible_coins[amount] if possible_coins[amount]!=float('inf') else -1

        