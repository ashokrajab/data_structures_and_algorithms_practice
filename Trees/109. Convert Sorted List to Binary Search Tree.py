"""
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a
height-balanced
binary search tree.

 

Example 1:

Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.

Example 2:

Input: head = []
Output: []

 

Constraints:

    The number of nodes in head is in the range [0, 2 * 104].
    -105 <= Node.val <= 105

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        node_list = []
        curr = head
        while curr:
            node_list.append(curr.val)
            curr = curr.next
        
        def dnc(l,r):
            if r-l < 0:
                return None
            if r-l == 0:
                leaf = TreeNode(node_list[r])
                return leaf

            m = (l+r) // 2

            left = dnc(l, m-1)
            right = dnc(m+1, r)
            node = TreeNode(node_list[m], left, right)
            return node
        
        return dnc(0, len(node_list)-1)
