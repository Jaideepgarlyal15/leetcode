# 322. Coin Change
# https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins, amount):
        def dp(i,amount):
            if amount==0:
                return 0
            if i==len(coins):
                return float('inf')
            if (i+1,amount) not in memo:
                memo[(i+1,amount)]=dp(i+1,amount)
            ans=memo[(i+1,amount)]
            if amount>=coins[i]:
                if (i,amount-coins[i]) not in memo:
                    memo[(i,amount-coins[i])]=dp(i,amount-coins[i])
                ans=min(ans,memo[(i,amount-coins[i])]+1)
            return ans
        memo={}
        x=dp(0,amount)
        return x if x!=float('inf') else -1

# obj=Solution()
# print(obj.coinChange(list(map(int,input().split())),int(input())))