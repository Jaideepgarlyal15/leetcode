# 64. Minimum Path Sum
# https://leetcode.com/problems/minimum-path-sum/

class Solution:
    def minPathSum(self, grid):
        
        r,c=len(grid),len(grid[0])
        dp=[[0]*(c) for _ in range(r)]
        dp[0][0]=grid[0][0]
        for i in range(1,r):
            dp[i][0]=dp[i-1][0]+grid[i][0]
        for i in range(1,c):
            dp[0][i]=dp[0][i-1]+grid[0][i]
        for i in range(1,r):
            for j in range(1,c):
                dp[i][j]=min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        return dp[-1][-1]
        '''
        # Space saving
        r,c=len(grid),len(grid[0])
        for i in range(1,r):
            grid[i][0]+=grid[i-1][0]
        for i in range(1,c):
            grid[0][i]+=grid[0][i-1]
        for i in range(1,r):
            for j in range(1,c):
                grid[i][j]+=min(grid[i-1][j],grid[i][j-1])
        return grid[-1][-1]
        '''


# # take input  
# obj=Solution()
# n=int(input())
# x=[]
# for _ in range(n):
#     x.append(list(map(int,input().split())))
# print(obj.minPathSum(x))