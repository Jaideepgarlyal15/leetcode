# 169. Majority Element
# https://leetcode.com/problems/majority-element/
import math
class Solution:
    def majorityElement(self, nums):
        x=math.floor(len(nums)/2)
        for i in list(set(nums)):
            if nums.count(i)>x:
                return i

        '''
        nums.sort()
        return nums[len(nums)//2]
        '''

        '''
        x=nums[0]
        count=1
        for i in range(1,len(nums)):
            if nums[i]==x:
                count+=1
            else:
                count-=1
            if count==0:
                x=nums[i]
                count=1
        return x
        '''

obj=Solution()
print(obj.majorityElement(list(map(int,input().split()))))