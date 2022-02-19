# 1770. Maximum Score from Performing Multiplication Operations
# https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/

# from functools import lru_cache

class Solution:
    def maximumScore(self, nums, multipliers):
        # Top-down
        @lru_cache(None)
        def dp(i,left):
            if i==len(multipliers):
                return 0
            mul=multipliers[i]
            right=len(nums)-1-(i-left)
            return max(mul*nums[left]+dp(i+1,left+1),mul*nums[right]+dp(i+1,left))
        return dp(0,0)
        '''
        # Bottom-Up
        n,m=len(nums),len(multipliers)
        dp=[[0]*(m+1) for _ in range(m+1)]
        for i in range(m-1,-1,-1):
            for left in range(i,-1,-1):
                right=n-1-(i-left)
                temp=multipliers[i]
                dp[i][left]=max(temp*nums[left]+dp[i+1][left+1],temp*nums[right]+dp[i+1][left])
        return dp[0][0]
        '''

# obj=Solution()
# print(obj.maximumScore(list(map(int,input().split())),list(map(int,input().split()))))