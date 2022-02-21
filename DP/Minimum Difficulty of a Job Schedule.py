# 1335. Minimum Difficulty of a Job Schedule
# https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/
class Solution:
    def minDifficulty(self, jobDifficulty, d):
        n=len(jobDifficulty)

        if n<d:
            return -1
        hard=[0]*(n)

        for i in range(n):
            hard[i]=max(jobDifficulty[i:])

        def dp(i,day):
            if day==d:
                return hard[i]
            best=float('inf')
            hardest=0
            for j in range(i,n-(d-day)):
                hardest=max(hardest,jobDifficulty[j])
                if (j+1,day+1) not in memo:
                    memo[(j+1,day+1)]=dp(j+1,day+1)
                best=min(best,memo[(j+1,day+1)]+hardest)
            return best

        memo={}
        return dp(0,1)

# obj=Solution()
# print(obj.minDifficulty(list(map(int,input().split())),int(input())))