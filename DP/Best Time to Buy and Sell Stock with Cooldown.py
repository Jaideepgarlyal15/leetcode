# 309. Best Time to Buy and Sell Stock with Cooldown
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

# from functools import lru_cache

class Solution:
    def maxProfit(self, prices):
        @lru_cache(None)
        def dp(idx,stock,cd):
            if idx==len(prices):
                return 0
            don=dp(idx+1,stock,0)
            dos=0
            if cd==1:
                cd=0
            elif stock:
                dos=dp(idx+1,0,1)+prices[idx]
            else:
                dos=dp(idx+1,1,0)-prices[idx]
            return max(don,dos)
        return dp(0,0,0)

# obj=Solution()
# print(obj.maxProfit(list(map(int,input().split()))))