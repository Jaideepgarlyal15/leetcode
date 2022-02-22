# 931. Minimum Falling Path Sum
# https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix):
        for i in range(1,len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j]+=min(matrix[i-1][j],matrix[i-1][min(j+1,len(matrix[0])-1)],matrix[i-1][max(0,j-1)])
        return min(matrix[-1])


# # take input  
# obj=Solution()
# n=int(input())
# x=[]
# for _ in range(n):
#     x.append(list(map(int,input().split())))
# print(obj.minFallingPathSum(x))