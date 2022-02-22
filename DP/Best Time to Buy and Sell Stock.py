# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices):
        buy=float('inf')
        profit=0
        for i in prices:
            buy=min(buy,i)
            profit=max(profit,i-buy)
        return profit


# obj=Solution()
# print(obj.maxProfit(list(map(int,input().split()))))