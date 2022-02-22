# 198. House Robber
# https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums):
        # Top-down
        def dp(i):
            if i==0:
                return nums[0]
            if i==1:
                return max(nums[0],nums[1])
            if i not in memo:
                memo[i]=max(dp(i-1),dp(i-2)+nums[i])
            return memo[i]
        memo={}
        return dp(len(nums)-1)
        
        '''
        Bottom-Up
        n=len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
        dp=[0]*(n)
        dp[0],dp[1]=nums[0],max(nums[0],nums[1])
        for i in range(2,n):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        return dp[-1]
        '''

# obj=Solution()
# print(obj.rob(list(map(int,input().split()))))