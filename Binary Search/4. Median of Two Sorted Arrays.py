"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

 

Constraints:

    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -106 <= nums1[i], nums2[i] <= 106
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        N1 = len(nums1)
        N2 = len(nums2)
        total = (N1+N2)
        half = total//2
        
        if N1 > N2:
            nums1,nums2 = nums2,nums1
            
        l=0
        r=len(nums1)-1
        while True:
            m1 = (l+r)//2
            m2 = half - m1 - 2
            
            nums1_left = nums1[m1] if m1 >= 0 else float("-infinity")
            nums1_right = nums1[m1 + 1] if m1+1 < len(nums1) else float("infinity")
            nums2_left = nums2[m2] if m2 >= 0 else float("-infinity")
            nums2_right = nums2[m2 + 1] if m2+1 < len(nums2) else float("infinity")
            
            #left partion is valid
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                #odd
                if total%2:
                    return min(nums1_right,nums2_right)
                #even
                else:
                    median = max(nums1_left,nums2_left) + min(nums1_right,nums2_right)
                    return median/2
            elif nums1_left > nums2_right:
                r = m1 - 1
            else:
                l = m1 + 1
            