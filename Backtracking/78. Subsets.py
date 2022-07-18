"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

Input: nums = [0]
Output: [[],[0]]

 

Constraints:

    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
    All the numbers of nums are unique.
"""
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        tmp = []
        def backtrack(idx):
            nonlocal ans
            if idx >= len(nums):
                ans.append(tmp[:])
                return
            
            tmp.append(nums[idx])
            backtrack(idx+1)
            tmp.pop()
            backtrack(idx+1)
                
        backtrack(0)
        return ans
            
            