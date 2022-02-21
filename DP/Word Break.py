# 139. Word Break
# https://leetcode.com/problems/word-break/

class Solution:
    def wordBreak(self, s, wordDict):
        dp=[0]*(len(s))
        for i in range(len(s)):
            for word in wordDict:
                if i>=len(word)-1 and (dp[i-len(word)] or i==len(word)-1):
                    if s[i-len(word)+1:i+1]==word:
                        dp[i]=1
                        break
        return bool(dp[-1])

# obj=Solution()
# print(obj.wordBreak(input(),list(map(str,input().split()))))