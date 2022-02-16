# 414. Third Maximum Number
# https://leetcode.com/problems/third-maximum-number/

class Solution:
    def thirdMax(self, nums):
        nums=list(set(nums))
        nums.sort(reverse=True)
        return nums[2] if len(nums)>2 else nums[0]

# print(Solution.thirdMax('self',list(map(int,input().split()))))