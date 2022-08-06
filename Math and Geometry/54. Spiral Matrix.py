"""
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

 

Constraints:

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 10
    -100 <= matrix[i][j] <= 100
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        TOP,BOTTOM,LEFT,RIGHT = 0,len(matrix),0,len(matrix[0])
        res = []
        
        while LEFT<RIGHT and TOP<BOTTOM:
            for i in range(LEFT,RIGHT):
                res.append(matrix[TOP][i])
            TOP +=1
            
            for i in range(TOP,BOTTOM):
                res.append(matrix[i][RIGHT-1])
            RIGHT -=1
            
            if not(LEFT<RIGHT and TOP<BOTTOM):
                break
                
            for i in range(RIGHT-1,LEFT-1,-1):
                res.append(matrix[BOTTOM-1][i])
            BOTTOM -=1
            
            for i in range(BOTTOM-1,TOP-1,-1):
                res.append(matrix[i][LEFT])
            LEFT +=1
        return res