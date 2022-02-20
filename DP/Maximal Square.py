# 221. Maximal Square
# https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, mat):
        r,c=len(mat),len(mat[0])
        dp=[[0]*(c+1) for _ in range(r+1)]
        ans=0
        for i in range(1,r+1):
            for j in range(1,c+1):
                if mat[i-1][j-1]==1:
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                    ans=max(ans,dp[i][j])
        return ans**2

# take input  
# obj=Solution()
# n=int(input())
# x=[]
# for _ in range(n):
#     x.append(list(map(int,input().split())))
# print(obj.maximalSquare(x))
