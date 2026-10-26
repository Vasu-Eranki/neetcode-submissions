class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum_value = 0 
        maxPrice = prices[-1]

        for idx in range(len(prices)-1,-1,-1):
            profit = maxPrice - prices[idx]
            if profit>maximum_value:
                maximum_value = profit
            if(prices[idx]>maxPrice):
                maxPrice = prices[idx]
        return maximum_value

        
        