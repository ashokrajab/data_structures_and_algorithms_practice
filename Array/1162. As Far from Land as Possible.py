"""
Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

 

Example 1:

Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.

Example 2:

Input: grid = [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.

 

Constraints:

    n == grid.length
    n == grid[i].length
    1 <= n <= 100
    grid[i][j] is 0 or 1

"""
from typing import List
from collections import deque
import sys
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        
        visited = set()   
        q = deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    q.append((i,j))
                    visited.add((i,j))
        dist = -1
        while q:
            dist += 1
            q_len = len(q)

            for _ in range(q_len):
                i,j = q.popleft()
                for di,dj in [(0,1),(1,0),(0,-1),(-1,0)]:
                    new_i = i+di
                    new_j = j+dj
                    if (new_i,new_j) not in visited and \
                        0 <= new_i < row and \
                        0 <= new_j < col:
                        q.append((new_i,new_j))
                        visited.add((new_i,new_j))
        return dist if dist >= 1 else -1