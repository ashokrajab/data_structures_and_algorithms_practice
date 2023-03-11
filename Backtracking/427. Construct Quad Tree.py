from typing import List

class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def dfs(r_min, r_max, c_min, c_max):
            if r_min == r_max or c_min == c_max:
                v = grid[r_min][c_min]
                node = Node(val=v, isLeaf=True, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None)
                return node
            
            tl_node = dfs(r_min, (r_min+r_max)//2, c_min, (c_min+c_max)//2)
            tr_node = dfs(r_min, (r_min+r_max)//2, (c_min+c_max)//2 +1, c_max)
            bl_node = dfs((r_min+r_max)//2 +1, r_max, c_min, (c_min+c_max)//2)
            br_node = dfs((r_min+r_max)//2 +1, r_max, (c_min+c_max)//2 +1, c_max)

            children_val_set = set([tl_node.val,
                                    tr_node.val,
                                    bl_node.val,
                                    br_node.val,])
            is_all_leaf = tl_node.isLeaf and tr_node.isLeaf and bl_node.isLeaf and br_node.isLeaf
            if is_all_leaf and len(children_val_set) == 1:
                v = children_val_set.pop()
                par_node = Node(val=v, isLeaf=True, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None)
            else:
                par_node = Node(val=1, isLeaf=False, topLeft=tl_node, topRight=tr_node, bottomLeft=bl_node, bottomRight=br_node)
            return par_node
        n = len(grid)
        return dfs(0, n-1, 0, n-1)
Solution().construct(grid = [[1,1,0,0],[0,0,1,1],[1,1,0,0],[0,0,1,1]])