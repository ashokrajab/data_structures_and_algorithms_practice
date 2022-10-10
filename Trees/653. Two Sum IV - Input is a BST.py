"""
Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

 

Example 1:

Input: root = [5,3,6,2,4,null,7], k = 9
Output: true

Example 2:

Input: root = [5,3,6,2,4,null,7], k = 28
Output: false

 

Constraints:

    The number of nodes in the tree is in the range [1, 104].
    -104 <= Node.val <= 104
    root is guaranteed to be a valid binary search tree.
    -105 <= k <= 105
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen_values = set()
        
        def pre_order_traversal(node):
            if not node:
                return False
            
            if (k - node.val) in seen_values:
                return True
            
            seen_values.add(node.val)
            found = pre_order_traversal(node.left)
            if found:
                return True
            found = pre_order_traversal(node.right)
            if found:
                return True
            return False
        return pre_order_traversal(root)
            