"""
You are given an m x n grid where each cell can have one of three values:

    0 representing an empty cell,
    1 representing a fresh orange, or
    2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 10
    grid[i][j] is 0, 1, or 2.
"""
from collections import deque
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        time,fresh = 0,0
        q = deque()
        ones_set = set()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        def bfs():
            nonlocal time,fresh
            while q and fresh>0:
                q_len = len(q)
                for i in range(q_len):
                    r,c = q.popleft()
                    for d in directions:
                        if (r+d[0] >=0 and c+d[1]>=0 
                        and r+d[0] <=ROW-1 and c+d[1] <=COL-1
                        and grid[r+d[0]][c+d[1]]==1):
                            q.append((r+d[0],c+d[1]))
                            grid[r+d[0]][c+d[1]] = 2
                            fresh -= 1
                time += 1
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c]==2:
                    q.append((r,c))
                elif grid[r][c]==1:
                    fresh += 1
        bfs()
        if fresh == 0:
            return time
        else:
            return -1
        