# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        leaves = []
        trees_dict = {}
        for tree in trees:
            trees_dict[tree.val] = tree
            if tree.left:
                if tree.left.val in leaves:
                    return None
                leaves.append(tree.left.val)
                
            if tree.right:
                if tree.right.val in leaves:
                    return None
                leaves.append(tree.right.val)
        
        root = None
        count = 0
        for tree in trees:
            if tree.val not in leaves:
                root = tree
                count += 1
        
        if not root or count > 1:
            return None
        
        current_leaves = {}
        
        if root.left:
            # tupe(low, high, parent_node, leftOrRight)
            current_leaves[root.left.val] = (-sys.maxsize, root.val, root, 0)
        if root.right:
            current_leaves[root.right.val] = (root.val, sys.maxsize, root, 1)
            
        del trees_dict[root.val]
        
        while trees_dict:
            foundTree = False
            for leaf_val, (low, high, parent_node, leftOrRight) in current_leaves.items():
                if leaf_val in trees_dict:
                    candidate_tree = trees_dict[leaf_val]
                    del current_leaves[leaf_val]
                    
                    if candidate_tree.left:
                        if low < candidate_tree.left.val < high:
                            current_leaves[candidate_tree.left.val] = (low, candidate_tree.val, candidate_tree, 0)
                        else:
                            return None
                            
                    if candidate_tree.right:
                        if low < candidate_tree.right.val < high:
                            current_leaves[candidate_tree.right.val] = (candidate_tree.val, high, candidate_tree, 1)
                        else:
                            return None
                
                    if leftOrRight == 0:
                        parent_node.left = candidate_tree
                    else:
                        parent_node.right = candidate_tree
                    foundTree = True
                    del trees_dict[candidate_tree.val]
                    break
            
            if not foundTree:
                return None
            
        return root