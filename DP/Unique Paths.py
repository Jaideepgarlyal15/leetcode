# 62. Unique Paths
# https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m, n):
        dp=[[1]*(n) for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[-1][-1]

        '''
        # Space saving
        dp=[1]*(n)
        for i in range(1,m):
            for j in range(1,n):
                dp[j]+=dp[j-1]
        return dp[-1]
        '''

# obj=Solution()
# x,y=input().split()
# print(obj.uniquePaths(int(x),int(y)))