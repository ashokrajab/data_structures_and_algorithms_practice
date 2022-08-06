"""
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:

Input: s = "a"
Output: [["a"]]

 

Constraints:

    1 <= s.length <= 16
    s contains only lowercase English letters.
"""
from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        parts = []
        
        def isPalindrome(s , l, r):
            while l<=r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True 
                
        def backtrack(i):
            if i == len(s):
                res.append(parts[:])
                return 
            
            for j in range(i, len(s)):
                if isPalindrome(s, i, j):
                    parts.append(s[i:j+1])
                    backtrack(j+1)
                    parts.pop()
        backtrack(0)       
        return res