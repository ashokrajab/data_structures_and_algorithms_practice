"""
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

 

Example 1:

Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Example 2:

Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3

 

Constraints:

    1 <= n <= 200
    n == isConnected.length
    n == isConnected[i].length
    isConnected[i][j] is 1 or 0.
    isConnected[i][i] == 1
    isConnected[i][j] == isConnected[j][i]
"""
class SubSets:
    def __init__(self, parent, rank=1):
        self.parent = parent
        self.rank = rank
    
class Solution:
    def find(self, n):
        if self.subsets[n].parent != n:
            self.subsets[n].parent = self.find(self.subsets[n].parent)
        return self.subsets[n].parent
    
    def union(self, n1_rep, n2_rep):
        if self.subsets[n1_rep].rank >= self.subsets[n2_rep].rank:
            self.subsets[n2_rep].parent = self.subsets[n1_rep].parent
            self.subsets[n1_rep].rank += self.subsets[n2_rep].rank
        else:
            self.subsets[n1_rep].parent = self.subsets[n2_rep].parent
            self.subsets[n2_rep].rank += self.subsets[n1_rep].rank

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.subsets = [SubSets(i) for i in range(len(isConnected))]
        total_connected_components = len(isConnected)
        
        for i in range(0, len(isConnected)):
            for j in range(i+1, len(isConnected[0])):
                if isConnected[i][j]:
                    i_rep = self.find(i)
                    j_rep = self.find(j)
                    
                    if i_rep != j_rep:
                        self.union(i_rep, j_rep)
                        total_connected_components -= 1
        return total_connected_components
        