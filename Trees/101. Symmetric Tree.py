"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:

Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:

Input: root = [1,2,2,null,3,null,3]
Output: false

 

Constraints:

    The number of nodes in the tree is in the range [1, 1000].
    -100 <= Node.val <= 100
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def isMirror(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            
            return node1.val == node2.val and isMirror(node1.left, node2.right) and isMirror(node1.right, node2.left)
        
        return isMirror(root.left, root.right)

class Solution2:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = []
        q.append(root)
        
        while q:
            q_len = len(q)
            for _ in range(q_len):
                node = q.pop(0)
                if not node:
                    continue
                q.append(node.left)
                q.append(node.right)
            
            l,r = 0,len(q)-1
            
            while l<r:
                if not q[l] and q[r]:
                    return False
                elif q[l] and not q[r]:
                    return False
                elif not q[l] and not q[r]:
                    pass
                elif q[l].val != q[r].val:
                    return False
                l += 1
                r -= 1
            
                
        return True
