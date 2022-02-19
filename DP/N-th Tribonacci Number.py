# 1137. N-th Tribonacci Number
# https://leetcode.com/problems/n-th-tribonacci-number/

class Solution:
    def tribonacci(self, n: int) -> int:
        def dp(i):
            if i==0:
                return 0
            if i==1 or i==2:
                return 1
            if i not in memo:
                memo[i]=dp(i-1)+dp(i-2)+dp(i-3)
            return memo[i]
        memo={}
        return dp(n)
        
        '''
        if n==0:
            return 0
        if n==1 or n==2:
            return 1
        x,y,z=0,1,1
        for i in range(2,n):
            a,b=z,y
            z=x+y+z
            y=a
            x=b
        return z
        '''

obj=Solution()
print(obj.tribonacci(int(input())))