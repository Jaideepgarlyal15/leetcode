# 123. Best Time to Buy and Sell Stock III
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/submissions/

# from functools import lru_cache

class Solution:
    def maxProfit(self, prices):
        @lru_cache(None)
        def dp(i,k,h):
            if i==len(prices) or k==0:
                return 0
            don=dp(i+1,k,h)
            dos=0
            if h:
                dos=dp(i+1,k-1,0)+prices[i]
            else:
                dos=dp(i+1,k,1)-prices[i]
            return max(don,dos)
        return dp(0,2,0)

# obj=Solution()
# print(obj.maxProfit(list(map(int,input().split()))))