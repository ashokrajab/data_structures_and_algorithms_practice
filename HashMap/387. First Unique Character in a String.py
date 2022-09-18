"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0

Example 2:

Input: s = "loveleetcode"
Output: 2

Example 3:

Input: s = "aabb"
Output: -1

 

Constraints:

    1 <= s.length <= 105
    s consists of only lowercase English letters.
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_vs_index = {}
        char_set = set()
        
        for i,c in enumerate(s):
            if c in char_set:
                if c in char_vs_index:
                    del char_vs_index[c]
            else:
                char_vs_index[c] = i
                char_set.add(c)
        
        for c,i in char_vs_index.items():
            return i
        
        return -1