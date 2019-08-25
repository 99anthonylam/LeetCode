# Link: https://leetcode.com/problems/coin-change/
# Level: Medium

# Runtime: 1236 ms, faster than 74.22% of Python3 online submissions for Coin Change.
# Memory Usage: 14 MB, less than 30.56% of Python3 online submissions for Coin Change.
    
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr = [0] + [sys.maxsize for i in range(amount)]  # no need for zero-indexing and you need 0 coins for $0
        for coin in coins:
            # go through all possible ways to make the diff between amt and each of the coins
            for i in range(coin, amount + 1):
                # either use current lowest # of coins (stored in arr[i]) or use curr coin (+1 to # of coins)
                arr[i] = min(arr[i], arr[i-coin]+1)  
        
        if arr[-1] == sys.maxsize:
            return -1
        return arr[-1]  # last entry in arr equates to min # of coins to get amount
