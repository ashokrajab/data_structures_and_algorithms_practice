"""
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

 

Example 1:

Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:

Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]

 

Constraints:

    The number of nodes in the linked list is in the range [0, 104].
    -106 <= Node.val <= 106
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        count = 0
        end = head
        
        while end.next:
            count += 1
            end = end.next
        
        isCountEven = count % 2 == 0
        
        limit = (count/2) if isCountEven else (count/2)+1
        temp = head
        i = 1
        while i <= limit:
            end.next = temp.next
            temp.next = temp.next.next
            
            end.next.next = None
            temp = temp.next
            end = end.next
            i += 1
        return head  
#         if not head:
#             return head
        
#         odd_head = head
#         even_head = head.next
        
#         odd_curr = odd_head
#         even_curr = even_head
        
        
#         while even_curr and even_curr.next:
#             odd_curr.next = odd_curr.next.next
#             odd_curr = odd_curr.next
#             even_curr.next = even_curr.next.next
#             even_curr = even_curr.next
        
#         odd_curr.next = even_head
        
#         return odd_head