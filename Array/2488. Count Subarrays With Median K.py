"""


You are given an array nums of size n consisting of distinct integers from 1 to n and a positive integer k.

Return the number of non-empty subarrays in nums that have a median equal to k.

Note:

    The median of an array is the middle element after sorting the array in ascending order. If the array is of even length, the median is the left middle element.
        For example, the median of [2,3,1,4] is 2, and the median of [8,4,3,5,1] is 4.
    A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [3,2,1,4,5], k = 4
Output: 3
Explanation: The subarrays that have a median equal to 4 are: [4], [4,5] and [1,4,5].

Example 2:

Input: nums = [2,3,1], k = 3
Output: 1
Explanation: [3] is the only subarray that has a median equal to 3.

 

Constraints:

    n == nums.length
    1 <= n <= 105
    1 <= nums[i], k <= n
    The integers in nums are distinct.

"""
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        diff = []
        index_k = None
        for i,n in enumerate(nums):
            if n < k:
                diff.append(-1)
            elif n > k:
                diff.append(1)
            else:
                index_k = i
                diff.append(0)
        
        suffix_sum = {0:1}
        curr_sum = 0
        for i in range(index_k+1, len(nums)):
            curr_sum += diff[i]
            suffix_sum[curr_sum] = suffix_sum.get(curr_sum,0)+1
        res = suffix_sum[0] + suffix_sum.get(1,0)
        curr_sum = 0
        for i in range(index_k-1,-1,-1):
            curr_sum += diff[i]
            res += (suffix_sum.get(-curr_sum,0) + suffix_sum.get(1-curr_sum,0))
        return res
        
        