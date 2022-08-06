"""
Given an undirected tree consisting of n vertices numbered from 1 to n. A frog starts jumping from vertex 1. In one second, the frog jumps from its current vertex to another unvisited vertex if they are directly connected. The frog can not jump back to a visited vertex. In case the frog can jump to several vertices, it jumps randomly to one of them with the same probability. Otherwise, when the frog can not jump to any unvisited vertex, it jumps forever on the same vertex.

The edges of the undirected tree are given in the array edges, where edges[i] = [ai, bi] means that exists an edge connecting the vertices ai and bi.

Return the probability that after t seconds the frog is on the vertex target. Answers within 10-5 of the actual answer will be accepted.

 

Example 1:

Input: n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 2, target = 4
Output: 0.16666666666666666 
Explanation: The figure above shows the given graph. The frog starts at vertex 1, jumping with 1/3 probability to the vertex 2 after second 1 and then jumping with 1/2 probability to vertex 4 after second 2. Thus the probability for the frog is on the vertex 4 after 2 seconds is 1/3 * 1/2 = 1/6 = 0.16666666666666666. 

Example 2:

Input: n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 1, target = 7
Output: 0.3333333333333333
Explanation: The figure above shows the given graph. The frog starts at vertex 1, jumping with 1/3 = 0.3333333333333333 probability to the vertex 7 after second 1. 

 

Constraints:

    1 <= n <= 100
    edges.length == n - 1
    edges[i].length == 2
    1 <= ai, bi <= n
    1 <= t <= 50
    1 <= target <= n


"""
from collections import defaultdict 
class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        def dfs(node, time, prob):
            nonlocal ans
            neighbours = graph[node]
            unvisited = [nei for nei in neighbours if nei not in visited]
            
            if time > t:
                return
            
            if node == target:
                if time == t or not unvisited:
                    ans = prob
                return
                
            if unvisited:
                p = 1 / len(unvisited)
                
            for nei in unvisited:
                visited.add(nei)
                dfs(nei, time+1, prob*p)
                visited.remove(nei)
                
            
        
        graph = defaultdict(list)
        
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        visited.add(1)
        ans = 0
        dfs(1,0,1)
        return ans
# class Solution:
#     def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
#         adjacency_matrix = [[0]*n for _ in range(n)]
        
#         for e in edges:
#             adjacency_matrix[e[0]-1][e[1]-1] = 1
#             adjacency_matrix[e[1]-1][e[0]-1] = 1
            
#         visited_nodes = []
#         q = collections.deque([[([0],1.0)]])
        
#         for h in range(t):
#             tup_list = q.popleft()
            
#             next_level = []
            
#             for tup in tup_list: 
#                 nodes_list = tup[0]
#                 prev_prob = tup[1]

#                 for node in nodes_list:
#                     next_nodes = []
#                     visited_nodes.append(node)

#                     s = 0
#                     for idx in range(n):
#                         v = adjacency_matrix[node][idx]
#                         if v == 0:
#                             continue

#                         if idx not in visited_nodes:
#                             s +=1
#                             next_nodes.append(idx)

#                     new_tup = ([node], prev_prob)
#                     if s != 0: 
#                         new_prob = prev_prob * (1/s)
#                         new_tup = (next_nodes, new_prob)
#                     next_level.append(new_tup)
            
#             q.extend([next_level])
            
#         tup_list = q.popleft()
#         goal = target - 1
#         for tup in tup_list:   
#             nodes_list = tup[0]
#             prob = tup[1]
#             if goal in nodes_list:
#                 return prob
#         return 0.0
        
            
            