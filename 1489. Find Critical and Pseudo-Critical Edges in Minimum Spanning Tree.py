"""
Given a weighted undirected connected graph with n vertices numbered from 0 to n - 1, and an array edges where edges[i] = [ai, bi, weighti] represents a bidirectional and weighted edge between nodes ai and bi. A minimum spanning tree (MST) is a subset of the graph's edges that connects all vertices without cycles and with the minimum possible total edge weight.

Find all the critical and pseudo-critical edges in the given graph's minimum spanning tree (MST). An MST edge whose deletion from the graph would cause the MST weight to increase is called a critical edge. On the other hand, a pseudo-critical edge is that which can appear in some MSTs but not all.

Note that you can return the indices of the edges in any order.

 

Example 1:

Input: n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
Output: [[0,1],[2,3,4,5]]
Explanation: The figure above describes the graph.
The following figure shows all the possible MSTs:

Notice that the two edges 0 and 1 appear in all MSTs, therefore they are critical edges, so we return them in the first list of the output.
The edges 2, 3, 4, and 5 are only part of some MSTs, therefore they are considered pseudo-critical edges. We add them to the second list of the output.

Example 2:

Input: n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
Output: [[],[0,1,2,3]]
Explanation: We can observe that since all 4 edges have equal weight, choosing any 3 edges from the given 4 will yield an MST. Therefore all 4 edges are pseudo-critical.

 

Constraints:

    2 <= n <= 100
    1 <= edges.length <= min(200, n * (n - 1) / 2)
    edges[i].length == 3
    0 <= ai < bi < n
    1 <= weighti <= 1000
    All pairs (ai, bi) are distinct.
"""
class Node:
    def __init__(self, parent):
        self.parent = parent
        self.rank = 1
        
class UnionFind:
    def __init__(self, n):
        self.unionSet = [Node(i) for i in range(n)]
        self.weight = 0
        self.edgesCount = 0
        self.totalVertices = n
        
    def canContinueUF(self):
        return self.edgesCount < self.totalVertices -1
    
    def find(self, val):
        if self.unionSet[val].parent != val:
            self.unionSet[val].parent = self.find(self.unionSet[val].parent)
        return self.unionSet[val].parent
    
    def union(self, n1, n2, w):
        n1_r = self.find(n1)
        n2_r = self.find(n2)
        
        if n1_r != n2_r:
            if self.unionSet[n1_r].rank >= self.unionSet[n2_r].rank:
                self.unionSet[n2_r].parent = self.unionSet[n1_r].parent
                self.unionSet[n1_r].rank += self.unionSet[n2_r].rank
            else:
                self.unionSet[n1_r].parent = self.unionSet[n2_r].parent
                self.unionSet[n2_r].rank += self.unionSet[n1_r].rank
            self.weight += w
            self.edgesCount += 1
        
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        
        noOfEdges= len(edges)
        #(weight, v1,v2, edge_index)
        sorted_edges = [(edges[i][2],edges[i][0],edges[i][1],i) for i in range(noOfEdges)]
        sorted_edges.sort()
        
        uf1 = UnionFind(n)
        
        for w,u,v,_ in sorted_edges:
            if uf1.canContinueUF():
                uf1.union(u,v,w)
            else:
                break
        mst_weight = uf1.weight
        ce, pce = [],[]
        for wi,a,b,i in sorted_edges:
            uf2 = UnionFind(n)
            for w,u,v,j in sorted_edges:
                if i == j:
                    continue

                if uf2.canContinueUF():
                    uf2.union(u,v,w)
                else:
                    break
            
            if uf2.weight > mst_weight or uf2.edgesCount < n-1:
                ce.append(i)
            else:
                uf3 = UnionFind(n)
                uf3.union(a,b,wi)
                
                for wk,g,h,_ in sorted_edges:
                    if uf3.canContinueUF():
                        uf3.union(g,h,wk)
                    else:
                        break
                
                if uf3.weight == mst_weight:
                    pce.append(i)
                    
        return ce, pce