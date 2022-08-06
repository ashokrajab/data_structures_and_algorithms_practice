"""
Given the head of a linked list, rotate the list to the right by k places.

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:

Input: head = [0,1,2], k = 4
Output: [2,0,1]

Constraints:

    The number of nodes in the list is in the range [0, 500].
    -100 <= Node.val <= 100
    0 <= k <= 2 * 109
"""
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        list_len = 1
        dummy = ListNode()
        curr = head
        while curr.next:
            list_len +=1
            curr = curr.next
        
        noOfRotations = k % list_len
        if  noOfRotations==0:
            return head
        
        tail = curr
        curr = head 
        pos = 0
        while curr:
            pos +=1
            if pos < (list_len - noOfRotations):
                curr = curr.next
            else:
                dummy.next = curr.next
                curr.next=None
                tail.next=head
                break
        return dummy.next