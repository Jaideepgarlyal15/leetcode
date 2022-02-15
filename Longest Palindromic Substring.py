class Solution:
    def longestPalindrome(self, l: str) -> str:
        n=len(l)
        ans=[]
        for i in range(n):
            for j in range(n-1,i-1,-1):
                if i-1<0:
                    x,y=l[i:j+1],l[j::-1]
                else:
                    x,y=l[i:j+1],l[j:max(i-1,-1):-1]
                print(f"x: {x},y: {y}")
                if x==y:
                    ans.append(l[i:j+1])
        print(ans)
        ans.sort(key=lambda x:len(x),reverse=True)
        return ans[0]

obj=Solution()
print(obj.longestPalindrome(input()))