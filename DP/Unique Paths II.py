# 63. Unique Paths II
# https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid[0][0]==1:
            return 0
        r,c=len(obstacleGrid),len(obstacleGrid[0])
        obstacleGrid[0][0]=1
        for i in range(1,r):
            obstacleGrid[i][0]=1 if ( obstacleGrid[i-1][0]==1 and obstacleGrid[i][0]==0) else 0
        for i in range(1,c):
            obstacleGrid[0][i]=1 if (obstacleGrid[0][i-1]==1 and obstacleGrid[0][i]==0) else 0
        for i in range(1,r):
            for j in range(1,c):
                if obstacleGrid[i][j]==1:
                    obstacleGrid[i][j]=0
                else:
                    obstacleGrid[i][j]=obstacleGrid[i-1][j]+obstacleGrid[i][j-1]
        return obstacleGrid[-1][-1]

# # take input  
# obj=Solution()
# n=int(input())
# x=[]
# for _ in range(n):
#     x.append(list(map(int,input().split())))
# print(obj.uniquePathsWithObstacles(x))