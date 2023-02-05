"""
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""

 

Constraints:

    1 <= str1.length, str2.length <= 1000
    str1 and str2 consist of English uppercase letters.
"""
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        s1 = len(str1)
        s2 = len(str2)

        ans = 0
        if s1 > s2:
            str1, str2 = str2, str1
            s1, s2 = s2, s1

        # iterate the shorted string
        for i in range(1,s1+1):
            if s1 % i == 0 and s2 % i == 0:
                q1 = s1 // i
                q2 = s2 // i
                if str1[:i] * q1 == str1 and str1[:i] * q2 == str2:
                    ans = i
        
        return str1[:ans] #if ans != -1 else ""

