'''2. Add Two Numbers
Solved
Medium
Topics
conpanies icon
Companies
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1,s2 = "",""

        while l1 or l2:
            if l1:
                s1 += str(l1.val)
                l1 = l1.next
            if l2:
                s2 += str(l2.val)
                l2 = l2.next

            
            

        s1 = s1[::-1]
        s2 = s2[::-1]

        s3 = str(int(s1) + int(s2))
        s3 = s3[::-1]

        l3 = ListNode()
        root = l3

        for l in range(len(s3)):
            l3.val = int(s3[l])
            if l == len(s3)-1:
                continue
            newNode = ListNode()
            l3.next = newNode
            l3 = l3.next
        
        l3 = None

        return root
