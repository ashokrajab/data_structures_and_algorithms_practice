class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        low,high = matrix[0][0],matrix[-1][-1]
        
        while low<high:
            mid = (low+high)//2
            
            if sum(bisect.bisect(row,mid) for row in matrix) < k:
                low = mid + 1
            else:
                high = mid
        return low
#         min_heap = []
#         heapq.heapify(min_heap)
#         ROW,COL = len(matrix), len(matrix[0])
#         for i in range(ROW):
#             for j in range(COL):
#                 heapq.heappush(min_heap,matrix[i][j])
        
#         for i in range(1,k+1):
#             val = heapq.heappop(min_heap)
#             if i==k:
#                 return val