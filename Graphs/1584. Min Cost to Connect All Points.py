"""
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

 

Example 1:

Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation: 

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.

Example 2:

Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18

 

Constraints:

    1 <= points.length <= 1000
    -106 <= xi, yi <= 106
    All pairs (xi, yi) are distinct.
"""
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        p_len = len(points)
        
        point_dict = {(points[i][0],points[i][1]): i for i in range(p_len)}
        
        def cal_manhat_dis(pt1, pt2):
            return abs(pt1[0]-pt2[0]) + abs(pt1[1]-pt2[1])
        
        pq = []
        heapify(pq)
        
        for i in range(p_len):
            for j in range(i+1,p_len):
                dist = cal_manhat_dis(points[i], points[j])
                heappush(pq, (dist, (point_dict[(points[i][0],points[i][1])], point_dict[(points[j][0],points[j][1])])) ) 
        
        cost = 0
        parent = [i for i in range(p_len)]
        rank = [1] * p_len
        
        def find(pt):
            if parent[pt] != pt:
                parent[pt] = find(parent[pt])
            return parent[pt]
        
        def union(pt1, pt2):
            if rank[pt1] >= rank[pt2]:
                parent[pt2] = pt1
                rank[pt1] += rank[pt2]
            else:
                parent[pt1] = pt2
                rank[pt2] += rank[pt1]
        
        while pq :
            val = heappop(pq)
            c = val[0]
            pt1,pt2 = val[1][0],val[1][1]
            
            rep_pt1 = find(pt1)
            rep_pt2 = find(pt2)
            
            if rep_pt1 != rep_pt2:
                union(rep_pt1, rep_pt2)
                cost +=c
        
        return cost
            