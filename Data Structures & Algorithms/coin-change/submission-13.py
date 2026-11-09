class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        dp = [0]+[float('inf')]*(amount+1)
        for idx in range(0,amount+1,1):
            for coin in coins:
                if (idx-coin)>=0:
                    dp[idx] = min(dp[idx],1+dp[idx-coin])
            
        value= dp[amount]
        print(dp)
        return value if value!=float('inf') else -1

        