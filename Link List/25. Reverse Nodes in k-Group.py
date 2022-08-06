"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:

Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

 

Constraints:

    The number of nodes in the list is n.
    1 <= k <= n <= 5000
    0 <= Node.val <= 1000
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1 
            curr = curr.next
        
        dummy = ListNode()
        prev_tail = dummy
        pos = 1
        
        prev = None
        curr = head
        end = length - (length % k)
        while pos <= end:
            prev_head = curr
            inner = 1
            
            while inner <= k:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
                
                pos += 1
                inner += 1
            
            prev_tail.next = prev
            prev_tail = prev_head
        
        prev_tail.next = curr
        
        return dummy.next