# 1675. Minimize Deviation in Array
# https://leetcode.com/problems/minimize-deviation-in-array/
from heapq import heapify, heappushpop
class Solution:
    def minimumDeviation(self, nums):
        m,temp=float('inf'),float('inf')
        for i in range(len(nums)):
            nums[i]=nums[i] if nums[i]%2==0 else nums[i]*2
            m=min(m,nums[i])
        nums=[-i for i in nums]
        heapify(nums)
        while nums[0]%2==0:
            temp=min(temp,-nums[0]-m)
            m=min(m,-nums[0]//2)
            heappushpop(nums,nums[0]//2)
        return min(temp,-nums[0]-m)




obj=Solution()
print(obj.minimumDeviation(list(map(int,input().split()))))