#题目：121.买卖股票的最佳时机
#难度：Easy
#日期：2026.6.4
#思路：从最低点买入，从最高点卖出，且卖出必须在买入之后
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for price in prices[1:]:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit
