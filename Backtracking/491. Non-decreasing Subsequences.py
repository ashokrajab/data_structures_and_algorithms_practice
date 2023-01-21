"""
Given an integer array nums, return all the different possible non-decreasing subsequences of the given array with at least two elements. You may return the answer in any order.

 

Example 1:

Input: nums = [4,6,7,7]
Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]

Example 2:

Input: nums = [4,4,3,2,1]
Output: [[4,4]]

 

Constraints:

    1 <= nums.length <= 15
    -100 <= nums[i] <= 100
"""
from typing import List
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        num_len = len(nums)
        def backtrack(i,stack):
            if i == num_len:
                if len(stack)>=2:
                    ans.add(tuple(stack[:]))
                return
            
            if stack and nums[i] < stack[-1]:
                backtrack(i+1, stack)
            else:
                stack.append(nums[i])
                backtrack(i+1, stack)
                stack.pop()
                backtrack(i+1, stack)
        backtrack(0,[])
        return ans 