# 24. Swap Nodes in Pairs
# https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head):
        a=head
        while a:
            if a.next:
                a.val,a.next.val=a.next.val,a.val
            a=a.next
            if a:
                a=a.next
        return head

# l=list(map(int,input().split()))  # take input as list
# root=ListNode(l.pop(0))   
# q=root

# while len(l)>0:   # make linked list from list
#     x=l.pop(0)
#     temp=ListNode(x)
#     q.next=temp
#     q=q.next

# obj=Solution()
# k=obj.swapPairs(root)     # slove problem
# while k:      # print answer
#     print(k.val,end=" ")
#     k=k.next