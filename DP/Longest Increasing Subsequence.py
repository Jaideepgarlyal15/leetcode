# 300. Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums):
        dp=[1]*(len(nums))
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)

# obj=Solution()
# print(obj.lengthOfLIS(list(map(int,input().split()))))