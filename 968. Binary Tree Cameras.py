"""
You are given the root of a binary tree. We install cameras on the tree nodes where each camera at a node can monitor its parent, itself, and its immediate children.

Return the minimum number of cameras needed to monitor all nodes of the tree.

 

Example 1:

Input: root = [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.

Example 2:

Input: root = [0,0,null,0,null,0,null,null,0]
Output: 2
Explanation: At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.

 

Constraints:

    The number of nodes in the tree is in the range [1, 1000].
    Node.val == 0


"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        
        
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        
        def dfs(node) -> bool:
            if not node:
                return False,True #camera,monitored
            
            c1,m1 = dfs(node.left)
            c2,m2 = dfs(node.right)
            
            c,m = False, False
            
            if c1 or c2:
                m = True
            
            if not m1 or not m2:
                c = True
                m = True
                self.count +=1
            
            return c,m
        
        c,m = dfs(root)
        if not m:
            return self.count + 1
        return self.count