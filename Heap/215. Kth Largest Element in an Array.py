class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-n for n in nums]
        heapify(heap)
        
        i=1
        while i<k:
            heappop(heap)
            i+=1
            
        return heappop(heap) * -1