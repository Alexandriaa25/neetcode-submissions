class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        lowest_price = prices[0]
        profit = 0


        for price in prices:
            if price < lowest_price:
                lowest_price = price
            
            curr_profit = price - lowest_price
            if curr_profit > profit:
                profit = curr_profit


          
        return profit