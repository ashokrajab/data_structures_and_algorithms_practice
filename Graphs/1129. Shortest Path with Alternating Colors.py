"""
You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

You are given two arrays redEdges and blueEdges where:

    redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
    blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.

Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.

 

Example 1:

Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
Output: [0,1,-1]

Example 2:

Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
Output: [0,1,-1]

 

Constraints:

    1 <= n <= 100
    0 <= redEdges.length, blueEdges.length <= 400
    redEdges[i].length == blueEdges[j].length == 2
    0 <= ai, bi, uj, vj < n


"""
from typing import List
from collections import deque, defaultdict
import sys
from typing import List
from collections import deque, defaultdict
import sys
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        red_graph = defaultdict(list)
        blue_graph = defaultdict(list)

        for u,v in redEdges:
            red_graph[u].append(v)
        for u,v in blueEdges:
            blue_graph[u].append(v)
        
        ans = [-1] * n
        visited = set((0,None)) # (node, visited_via_colour)
        q = deque()
        q.append([0,0,None]) # (node, distance, prev_colour)

        while q:
            node, distance, prev_colour = q.popleft()
            if ans[node] == -1:
                ans[node] = distance

            if prev_colour != "RED":
                for nei in red_graph[node]:
                    if (nei, "RED") not in visited:
                        visited.add((nei, "RED"))
                        q.append([nei, distance+1, "RED"])
                        
            if prev_colour != "BLUE":
                for nei in blue_graph[node]:
                    if (nei, "BLUE") not in visited:
                        visited.add((nei, "BLUE"))
                        q.append([nei, distance+1, "BLUE"])
                        
        return ans






# class Solution:
#     def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

#         def get_opp_col(col):
#             if col == "red":
#                 return "blue"
#             elif col == "blue":
#                 return "red"
#             else:
#                 return None

#         ans = [sys.maxsize] * n
#         ans[0] = 0

#         graph = defaultdict(dict)

#         for u,v in redEdges:
#             graph[u].update({v:set(["red"])})
        
#         for u,v in blueEdges:
#             if u in graph and v in graph[u].keys():
#                 col = graph[u][v]
#                 col.add("blue")
#                 graph[u].update({v:col})
#             else:
#                 graph[u].update({v:set(["blue"])})
        
#         q = deque([(0, "neutral")])
#         dist = 0
#         visited = set([(0,"neutral")])
#         while q:
#             q_len = len(q)
#             dist += 1
#             for _ in range(q_len):
#                 node, prev_col = q.popleft()
#                 for nei, col_set in graph[node].items():
#                     opp_col = get_opp_col(prev_col)
#                     if opp_col == None:
#                         for curr_col in col_set:
#                             visited.add((nei, curr_col))
#                             q.append((nei, curr_col))
#                         ans[nei] = min(ans[nei],dist)
#                     elif opp_col in col_set and (nei, opp_col) not in visited:
#                         visited.add((nei, opp_col))
#                         ans[nei] = min(ans[nei],dist)
#                         q.append((nei, opp_col))
#         for i, val in enumerate(ans):
#             if val == sys.maxsize:
#                 ans[i] = -1
#         return ans