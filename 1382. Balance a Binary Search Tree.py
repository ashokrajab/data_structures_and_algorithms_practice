# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

 

Example 1:

Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.

Example 2:

Input: root = [2,1,3]
Output: [2,1,3]

 

Constraints:

    The number of nodes in the tree is in the range [1, 104].
    1 <= Node.val <= 105

"""
        
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        sorted_list = []
        
        def dfs(node):
            if not node:
                return
            nonlocal sorted_list
            dfs(node.left)
            sorted_list.append(node.val)
            dfs(node.right)
        dfs(root)
        def createBST(l,r):
            if l>r:
                return None
            m = (l+r)//2
            node = TreeNode(sorted_list[m])
            node.left = createBST(l,m-1)
            node.right = createBST(m+1,r)
            return node
        
        return createBST(0,len(sorted_list)-1)
    