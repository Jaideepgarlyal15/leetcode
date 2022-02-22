# 918. Maximum Sum Circular Subarray
# https://leetcode.com/problems/maximum-sum-circular-subarray/

class Solution:
    def maxSubarraySumCircular(self, nums):
        def kadane(nums):
            best=nums[0]
            current_sum=nums[0]
            for i in nums[1:]:
                current_sum=max(i,current_sum+i)
                best=max(best,current_sum)
            return best
        
        total_sum=sum(nums)
        original_sum=kadane(nums)
        circular_sum=total_sum+kadane([-i for i in nums])
        if circular_sum==0:
            return original_sum
        return max(original_sum,circular_sum)

# obj=Solution()
# print(obj.maxSubarraySumCircular(list(map(int,input().split()))))