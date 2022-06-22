"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

 

Example 1:

Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 50
    grid[i][j] is either 0 or 1.
"""
class Node():
    def __init__(self, i,j, rank=1):
        self.pi = i
        self.pj = j
        self.rank = rank

class Solution:
    def find(self, n):
        parent = self.nodes[n.pi][n.pj]
        if not (parent.pi == n.pi and parent.pj == n.pj):
            self.nodes[n.pi][n.pj] = self.find(parent)
        return self.nodes[n.pi][n.pj]
    
    def union(self, n1, n2):
        if n1.rank >= n2.rank:
            n1.rank += n2.rank
            self.nodes[n2.pi][n2.pj] = n1
            self.ans = max(self.ans, n1.rank)
        else:
            n2.rank += n1.rank
            self.nodes[n1.pi][n1.pj] = n2
            self.ans = max(self.ans, n2.rank)
    
    def hasSameParent(self, n1, n2):
        n1_node = self.nodes[n1.pi][n1.pj]
        n2_node = self.nodes[n2.pi][n2.pj]
        return n1_node.pi == n2_node.pi and n1_node.pj == n2_node.pj
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        self.nodes = []
        for i in range(m):
            tmp = []
            for j in range(n):
                tmp.append(Node(i,j))
            self.nodes.append(tmp)
                
        self.ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    curr_node = self.nodes[i][j]
                    behind_node = None
                    top_node = None
                    if i-1 >=0 and grid[i-1][j]==1:
                        top_node = self.nodes[i-1][j]
                    if j-1 >=0 and grid[i][j-1]==1:
                        behind_node = self.nodes[i][j-1]
                    
                    if behind_node == None and top_node == None:
                        self.ans = max(self.ans, curr_node.rank)
                        continue
                    elif behind_node != None and top_node == None:
                        b_rep = self.find(behind_node)
                        self.union(b_rep, curr_node)
                    elif behind_node == None and top_node != None:
                        t_rep = self.find(top_node)
                        self.union(t_rep, curr_node)
                    else:
                        b_rep = self.find(behind_node)
                        t_rep = self.find(top_node)
                        if self.hasSameParent(b_rep, t_rep):
                            self.union(b_rep, curr_node)
                        else:
                            if b_rep.rank >= t_rep.rank:
                                self.union(b_rep, curr_node)
                                self.union(b_rep, t_rep)
                            else:
                                self.union(t_rep, curr_node)
                                self.union(t_rep, b_rep)
        
        return self.ans