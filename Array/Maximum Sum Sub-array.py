"""
Q: Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23

Constraints:
    1 <= nums.length <= 105
    -104 <= nums[i] <= 104
"""
# Kadane's algorithm
class Solution:
	def maxSubArray(self, nums: list[int]) -> int:
		max_sum = nums[0]
		cur_sum = nums[0]
		for i in range(1, len(nums)):
			cur_sum = max(nums[i], cur_sum + nums[i])
			max_sum = max(max_sum, cur_sum)
		return max_sum

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
