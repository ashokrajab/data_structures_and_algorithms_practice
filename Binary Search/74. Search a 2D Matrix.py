"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.

 

Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

 

Constraints:

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 100
    -104 <= matrix[i][j], target <= 104
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = len(matrix), len(matrix[0]) 
        def get_matrix_val(m):
            r = m//COL
            c = m-(r*COL)
            return matrix[r][c]
        
        def binary_search(l,r):
            m = (l+r)//2
            matrix_val_at_m = get_matrix_val(m)
            if matrix_val_at_m == target:
                return True
            if l >= r:
                return False
            if target < matrix_val_at_m:
                return binary_search(l,m-1)
            else:
                return binary_search(l+1,r)
        
        return binary_search(0,(ROW*COL)-1)