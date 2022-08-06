"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

 

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:

Input: s = ""
Output: 0

 

Constraints:

    0 <= s.length <= 3 * 104
    s[i] is '(', or ')'.
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        s_len = len(s)
        global_max = 0
        for i in range(s_len):
            b = s[i]
            if b == "(":
                stack.append(i)
            else:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i)
                else:
                    l = i - stack[-1]
                    global_max = max(global_max,l)
        return global_max
                


class Solution2:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        open_b = 0
        close_b = 0
        
        for c in s:
            if c == "(":
                open_b +=1
            else:
                close_b +=1
            
            if open_b == close_b:
                length = open_b + close_b
                max_len = max(max_len, length)
            elif close_b > open_b:
                close_b = open_b = 0
                
        open_b = 0
        close_b = 0
        for i in range(len(s)-1,-1,-1):
            c = s[i]
            if c == "(":
                open_b +=1
            else:
                close_b +=1
            
            if open_b == close_b:
                length = open_b + close_b
                max_len = max(max_len, length)
            elif close_b < open_b:
                close_b = open_b = 0
                
        return max_len