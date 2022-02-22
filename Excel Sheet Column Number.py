# 171. Excel Sheet Column Number
# https://leetcode.com/problems/excel-sheet-column-number/

class Solution:
    def titleToNumber(self, c):
        n=len(c)-1
        ans=0
        for i in range(n,-1,-1):
            ans+=((ord(c[i])-64)*(26**(n-i)))
        return ans

# obj=Solution()
# print(obj.titleToNumber(input()))