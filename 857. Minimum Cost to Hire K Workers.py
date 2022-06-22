"""
There are n workers. You are given two integer arrays quality and wage where quality[i] is the quality of the ith worker and wage[i] is the minimum wage expectation for the ith worker.

We want to hire exactly k workers to form a paid group. To hire a group of k workers, we must pay them according to the following rules:

    Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.
    Every worker in the paid group must be paid at least their minimum wage expectation.

Given the integer k, return the least amount of money needed to form a paid group satisfying the above conditions. Answers within 10-5 of the actual answer will be accepted.

 

Example 1:

Input: quality = [10,20,5], wage = [70,50,30], k = 2
Output: 105.00000
Explanation: We pay 70 to 0th worker and 35 to 2nd worker.

Example 2:

Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3
Output: 30.66667
Explanation: We pay 4 to 0th worker, 13.33333 to 2nd and 3rd workers separately.

 

Constraints:

    n == quality.length == wage.length
    1 <= k <= n <= 104
    1 <= quality[i], wage[i] <= 104
"""
class Solution:
    def maxHeapPush(self, val):
        heappush(self.pq, -val)
        
    def maxHeapPop(self):
        val = heappop(self.pq)
        return -val
    
    def maxHeapPeek(self):
        return -self.pq[0]
    
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        ratio_and_quality = []
        for w,q in zip(wage,quality):
            ratio = w/q
            ratio_and_quality.append((ratio,q))
            
        ratio_and_quality.sort()
        
        self.pq = []
        heapify(self.pq)
        
        quality_sum = 0
        for i in range(0,k):
            i_th_quality = ratio_and_quality[i][1]
            self.maxHeapPush(i_th_quality)
            quality_sum += i_th_quality
        
        captain_ratio = ratio_and_quality[k-1][0]
        minCost = quality_sum * captain_ratio
        
        for i in range(k,len(wage)):
            captain_ratio = ratio_and_quality[i][0]
            captain_quality = ratio_and_quality[i][1]
            if self.pq and captain_quality < self.maxHeapPeek():
                quality_sum -= self.maxHeapPop()
                self.maxHeapPush(captain_quality)
                quality_sum += captain_quality
            cost = quality_sum * captain_ratio
            minCost = min(minCost, cost)
        
        return minCost