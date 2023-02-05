"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

 

Constraints:

    1 <= s.length, p.length <= 3 * 104
    s and p consist of lowercase English letters.


"""
from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s = len(s)
        len_p = len(p)

        if len_s < len_p:
            return []
        
        s_list = [0] * 26
        p_list = [0] * 26

        for i in range(len_p):
            s_list[ord(s[i]) - ord('a')] += 1
            p_list[ord(p[i]) - ord('a')] += 1

        matches = 0
        for p_char_count, s_char_count in zip(p_list, s_list):
            if p_char_count == s_char_count:
                matches += 1
        
        ans = []
        if matches == 26:
            ans.append(0)
        
        for i in range(len_p, len_s):
            r_index = ord(s[i]) - ord('a') # char index when increasing the window
            l_index = ord(s[i-len_p]) - ord('a') # char index when decreasing the window

            r_index_match_before_slide = s_list[r_index] == p_list[r_index]
            l_index_match_before_slide = s_list[l_index] == p_list[l_index]

            s_list[r_index] += 1
            s_list[l_index] -= 1

            if s_list[r_index] == p_list[r_index]:
                if not r_index_match_before_slide:
                    matches += 1
            else:
                if r_index_match_before_slide:
                    matches -= 1
            if l_index != r_index:
                if s_list[l_index] == p_list[l_index]:
                    if not l_index_match_before_slide:
                        matches += 1
                else:
                    if l_index_match_before_slide:
                        matches -= 1
            if matches == 26:
                ans.append(i-len_p+1)
        return ans