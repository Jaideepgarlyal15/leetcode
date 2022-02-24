# 148. Sort List
# https://leetcode.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def sortList(self, head):
        ''' 
        if not head:
            return head
        l=[]
        temp=head
        while temp:
            l.append(temp.val)
            temp=temp.next
        l.sort()
        ans=ListNode(l[0])
        temp=ans
        for i in range(1,len(l)):
            temp.next=ListNode(l[i])
            temp=temp.next
        return ans
        ''' 
        if not head or not head.next:
            return head
        fast,slow=head.next,head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        start=slow.next
        slow.next=None
        l,r=self.sortList(head),self.sortList(start)
        return self.merge(l,r)

    def merge(self,l,r):
        if not l or not r:
            return l or r
        dummy=p=ListNode(0)
        while l and r:
            if l.val<r.val:
                p.next=l
                l=l.next
            else:
                p.next=r
                r=r.next
            p=p.next
        p.next=l or r
        return dummy.next


# obj=Solution()        # take input
# x=list(map(int,input().split()))
# root=ListNode(0)
# temp=root
# for i in range(len(x)):
#     temp.next=ListNode(x[i])
#     temp=temp.next
# ans=obj.sortList(root.next)
# while ans:            # print output
#     print(ans.val,end=" ")
#     ans=ans.next