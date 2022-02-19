# 746. Min Cost Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/
from tkinter import Y


class Solution:
    def minCostClimbingStairs(self, cost):
        # Top-down
        if len(cost)<=2:
            return 0
        def dp(i):
            if i==1 or i==0:
                return cost[i]
            if i not in memo:
                memo[i]=min(dp(i-1),dp(i-2))+cost[i]
            return memo[i]
        memo={}
        return min(dp(len(cost)-1),dp(len(cost)-2))

        '''
        Bottom-Up
        if len(cost)<=2:
            return 0
        dp=[0]*(len(cost))
        dp[0],dp[1]=cost[0],cost[1]
        for i in range(2,len(cost)):
            dp[i]=min(dp[i-1],dp[i-2])+cost[i]
        return min(dp[-1],dp[-2])
        '''

        '''
        Space saving
        if len(cost)<=2:
            return 0
        x,y=cost[0],cost[1]
        for i in range(2,len(cost)):
            temp=y
            y=min(x,y)+cost[i]
            x=temp
        return min(x,y)
        '''

obj=Solution()
print(obj.minCostClimbingStairs(list(map(int,input().split()))))