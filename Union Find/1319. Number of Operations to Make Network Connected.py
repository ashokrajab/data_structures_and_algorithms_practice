"""
There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.

 

Example 1:

Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.

Example 2:

Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2

Example 3:

Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
Explanation: There are not enough cables.

 

Constraints:

    1 <= n <= 105
    1 <= connections.length <= min(n * (n - 1) / 2, 105)
    connections[i].length == 2
    0 <= ai, bi < n
    ai != bi
    There are no repeated connections.
    No two computers are connected by more than one cable.
"""
class UnionFind:

    def __init__(self):
        self.par = {}
        self.rank = defaultdict(int)
    
    def find(self, node):
        if node not in self.par:
            self.par[node] = node
        elif self.par[node] != node:
            self.par[node] = self.find(self.par[node])
        return self.par[node]
    
    def union(self, n1, n2):
        par1 = self.find(n1)
        par2 = self.find(n2)

        if par1 != par2:
            if self.rank[par1] >= self.rank[par2]:
                self.par[par2] = par1
                self.rank[par1] += self.rank[par2]
            else:
                self.par[par1] = par2
                self.rank[par2] += self.rank[par1]
    
    def get_no_of_connected_components(self):
        ans = 0
        for par,child in self.par.items():
            if par == child:
                ans += 1
        return ans
    
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        if len(connections) < n-1:
            return -1

        uf = UnionFind()
        for u,v in connections:
            uf.union(u,v)
        
        connected_nodes = len(uf.par)
        isolated_nodes = n - connected_nodes

        no_of_connected_components = uf.get_no_of_connected_components()

        no_of_rewiring_req = no_of_connected_components + isolated_nodes -1 

        return no_of_rewiring_req