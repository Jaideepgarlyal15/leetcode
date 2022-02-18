# 402. Remove K Digits
# https://leetcode.com/problems/remove-k-digits/
class Solution:
    def removeKdigits(self, s: str, k: int) -> str:
        stack=[]
        for i in s:
            while stack and k and i<stack[-1]:
                k-=1
                stack.pop()
            stack.append(i)
        ans="".join(i for i in stack[:-k or None]).lstrip('0') or '0'
        return ans