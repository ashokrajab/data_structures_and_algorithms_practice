"""
We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some other people, and they should not go into the same group.

Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in this way.

 

Example 1:

Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4] and group2 [2,3].

Example 2:

Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false

Example 3:

Input: n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false

 

Constraints:

    1 <= n <= 2000
    0 <= dislikes.length <= 104
    dislikes[i].length == 2
    1 <= dislikes[i][j] <= n
    ai < bi
    All the pairs of dislikes are unique.

"""
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        def isBipartite(graph:Dict[int,int], node:int, colour:List[int]) -> bool:
            colour[node] = 1
            q = deque()
            q.append(node)
            
            while len(q) > 0:
                curr = q.popleft()
                
                for neighbour in graph[curr]:
                    
                    if colour[neighbour] == -1:
                        colour[neighbour] = int(not colour[curr])
                        q.append(neighbour)
                    elif colour[curr] == colour[neighbour]:
                        return False
            return True
                
            
        graph = defaultdict(list)
        
        for u,v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        
        colour = [-1] * (n+1)
        
        for i in range(1,n+1):
            if colour[i] == -1 and not isBipartite(graph, i, colour):
                return False
        
        return True
        