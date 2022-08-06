class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        pos = 0
        curr = head
        dummy = ListNode(0, head)
        begin = head
        begin_prev = dummy
        end = None
        end_prev = None
        while curr:
            pos +=1
            if pos == k:
                end = head
                end_prev = dummy
            elif pos >k:
                end_prev = end
                end = end.next
            else:#pos <k
                begin_prev = curr
                begin = begin_prev.next
            curr = curr.next
            
        begin_prev.next = end
        end_prev.next = begin
        
        tmp = end.next
        end.next = begin.next
        begin.next = tmp
        return dummy.next