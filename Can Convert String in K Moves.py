# 1540. Can Convert String in K Moves
# https://leetcode.com/problems/can-convert-string-in-k-moves/

class Solution:
    def canConvertString(self, s, t, k):
        if len(s)!=len(t):
            return False
        count=[0]*26
        for i in range(len(s)):
            diff=(ord(t[i])-ord(s[i]))%26
            if diff>0 and (count[diff]*26+diff)>k:
                return False
            count[diff]+=1
        return True

obj=Solution()
print(obj.canConvertString(input(),input(),int(input())))