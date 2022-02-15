# 5. Longest Palindromic Substring
# link: https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, l: str) -> str:
        start,size=0,1
        for i in range(len(l)):
            right=i
            while right<len(l) and l[i]==l[right]:
                right+=1
            left=i-1
            while left>=0 and right<len(l) and l[left]==l[right]:
                left-=1
                right+=1
            temp=-left+right-1
            if temp>size:
                size=temp
                start=left+1
        return l[start:start+size]

# obj=Solution()
# print(obj.longestPalindrome(input()))