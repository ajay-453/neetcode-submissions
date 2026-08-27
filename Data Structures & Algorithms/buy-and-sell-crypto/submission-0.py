class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        if len(prices) == 0 or len(prices) == 1:
            return 0
        else:
            min_price = prices[0]
            max_profit = 0
            profit =0
            while right < len(prices):

                if prices[right] < min_price :
                    min_price = prices[right]
                    left = right
                    right+=1
                else:
                    profit = prices[right] - min_price
                    right+= 1
                    max_profit  = max(max_profit, profit)

            return max_profit