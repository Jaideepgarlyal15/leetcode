# 188. Best Time to Buy and Sell Stock IV
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

# from functools import lru_cache

class Solution:
    def maxProfit(self, k, prices):
        @lru_cache(None)
        def dp(i,k,h):
            if k==0 or i==len(prices):
                return 0
            don=dp(i+1,k,h)
            dos=0
            if h:
                dos=dp(i+1,k-1,0)+prices[i]
            else:
                dos=dp(i+1,k,1)-prices[i]
            return max(don,dos)
        return dp(0,k,0)

# obj=Solution()
# print(obj.maxProfit(int(input()),list(map(int,input().split()))))