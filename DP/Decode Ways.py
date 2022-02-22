# 91. Decode Ways
# https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s):
        if s[0]=='0':
            return 0
        dp=[0]*(len(s)+1)
        dp[0]=dp[1]=1
        for i in range(1,len(s)):
            dp[i+1]=dp[i] if s[i]!='0' else 0
            if s[i-1]!='0' and int(s[i-1]+s[i])<=26:
                dp[i+1]+=dp[i-1]
        return dp[-1]

# obj=Solution()
# print(obj.numDecodings(input()))