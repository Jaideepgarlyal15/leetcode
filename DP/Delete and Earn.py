# 740. Delete and Earn
# https://leetcode.com/problems/delete-and-earn/

from functools import lru_cache


class Solution:
    def deleteAndEarn(self, nums):
        l=[0]*(10001)
        for i in nums:
            l[i]+=i
        def dp(i):
            if i==0:
                return l[0]
            if i==1:
                return max(l[0],l[1])
            if i not in memo:
                memo[i]=max(dp(i-1),dp(i-2)+l[i])
            return memo[i]
        memo={}
        return dp(len(l)-1)

# obj=Solution()
# print(obj.deleteAndEarn(list(map(int,input().split()))))