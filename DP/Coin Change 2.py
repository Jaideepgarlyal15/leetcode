# 518. Coin Change 2
# https://leetcode.com/problems/coin-change-2/

class Solution:
    def change(self, coins, amount):       
        dp=[0]*(amount+1)
        dp[0]=1
        for value in coins:
            for i in range(value,amount+1):
                dp[i]+=dp[i-value]
        return dp[amount]


# obj=Solution()
# print(obj.change(list(map(int,input().split())),int(input())))