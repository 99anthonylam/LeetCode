# Runtime: 72 ms, faster than 78.00% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 14.9 MB, less than 5.75% of Python3 online submissions for Best Time to Buy and Sell Stock.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if (len(prices) == 0):
            return 0
        lowest = prices[0]
        highest = 0
        for val in prices:
            if val < lowest:
                lowest = val
            if val - lowest > highest:
                highest = val - lowest
        return highest
