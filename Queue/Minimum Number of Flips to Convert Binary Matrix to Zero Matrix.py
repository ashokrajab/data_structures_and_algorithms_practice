"""
1284. Minimum Number of Flips to Convert Binary Matrix to Zero Matrix
Hard

Given a m x n binary matrix mat. In one step, you can choose one cell and flip it and all the four neighbors of it if they exist (Flip is changing 1 to 0 and 0 to 1). A pair of cells are called neighbors if they share one edge.

Return the minimum number of steps required to convert mat to a zero matrix or -1 if you cannot.

A binary matrix is a matrix with all cells equal to 0 or 1 only.

A zero matrix is a matrix with all cells equal to 0.

 

Example 1:

Input: mat = [[0,0],[0,1]]
Output: 3
Explanation: One possible solution is to flip (1, 0) then (0, 1) and finally (1, 1) as shown.

Example 2:

Input: mat = [[0]]
Output: 0
Explanation: Given matrix is a zero matrix. We do not need to change it.

Example 3:

Input: mat = [[1,0,0],[1,0,0]]
Output: -1
Explanation: Given matrix cannot be a zero matrix.

 

Constraints:

    m == mat.length
    n == mat[i].length
    1 <= m, n <= 3
    mat[i][j] is either 0 or 1.
"""
from collections import deque 
class Solution:
    def minFlips(self, mat: list[list[int]]) -> int:
        m,n = len(mat),len(mat[0])
        queue = deque()
        queue.append(mat)
        visited = set()
        step = 0

        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if sum(map(sum, node)) == 0:
                    return step

                for i in range(m):
                    for j in range(n):
                        flipped_node = self.flip_node(node, i, j)
                        immutable_flipped_node = tuple(map(tuple, flipped_node))

                        if immutable_flipped_node in visited:
                            continue

                        visited.add(immutable_flipped_node)
                        queue.append(flipped_node)
            step+=1
        return -1
    
    def  flip_node(self, node, i, j):
        copied_node = copy.deepcopy(node)
        m,n = len(node),len(node[0])
        copied_node[i][j] ^=1

        for dx, dy in [(-1,0), (1,0), (0,1), (0,-1)]:
            x = i +dx
            y = j +dy
            if x <0 or x >=m or y<0 or y>=n:
                continue
            copied_node[x][y] ^=1
        return copied_node