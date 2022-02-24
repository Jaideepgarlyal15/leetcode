# 122. Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices):
        ans=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                ans+=(prices[i]-prices[i-1])
        return ans

# obj=Solution()
# print(obj.maxProfit(list(map(int,input().split()))))