"""
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

Example 1:

Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

Example 2:

Input: heights = [[2,1],[1,2]]
Output: [[0,0],[0,1],[1,0],[1,1]]

 

Constraints:

    m == heights.length
    n == heights[r].length
    1 <= m, n <= 200
    0 <= heights[r][c] <= 105
"""
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])
        pac,atl = set(),set()
        res = []
        
        def dfs(r,c, visited, prev_ht):
            if r<0 or c<0 or r==ROW or c==COL or (r,c) in visited or heights[r][c] < prev_ht:
                return
            
            visited.add((r,c))
            dfs(r+1,c, visited, heights[r][c])
            dfs(r-1,c, visited, heights[r][c])
            dfs(r,c+1, visited, heights[r][c])
            dfs(r,c-1, visited, heights[r][c])
        
        for c in range(COL):
            dfs(0,c, pac, heights[0][c])
            dfs(ROW-1,c, atl, heights[ROW-1][c])
            
        for r in range(ROW):
            dfs(r,0, pac, heights[r][0])
            dfs(r,COL-1, atl, heights[r][COL-1])
            
        for r in range(ROW):
            for c in range(COL):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
            
        return res