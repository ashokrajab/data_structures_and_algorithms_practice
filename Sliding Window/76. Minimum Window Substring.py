"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

Constraints:

    m == s.length
    n == t.length
    1 <= m, n <= 105
    s and t consist of uppercase and lowercase English letters.
"""
from sys import maxsize
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t) or len(t) ==0:
            return ""

        t_map,s_map = {}, {}
        for c in t:
            t_map[c] = 1 + t_map.get(c,0)
        
        have = 0
        need = len(t_map)
        l = 0
        res = [-1, -1]
        res_len = maxsize
        for r in range(len(s)):
            char = s[r]
            if t_map.get(char, None) != None:#update s_map when its target char
                s_map[char] = 1 + s_map.get(char, 0)
                if s_map[char] == t_map[char]:
                    have += 1
                
            while have == need:
                if (r-l+1) < res_len:
                    res = [l ,r]
                    res_len = (r-l+1)

                pop_val = s[l]
                l += 1
                if s_map.get(pop_val, None) != None:
                    s_map[pop_val] -= 1
                    if s_map[pop_val] < t_map[pop_val]:
                        have -= 1
        l, r = res[0], res[1]
        return s[l:r+1] if res_len != maxsize else ""