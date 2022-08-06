"""
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

    Any left parenthesis '(' must have a corresponding right parenthesis ')'.
    Any right parenthesis ')' must have a corresponding left parenthesis '('.
    Left parenthesis '(' must go before the corresponding right parenthesis ')'.
    '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

 

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "(*)"
Output: true

Example 3:

Input: s = "(*))"
Output: true

 

Constraints:

    1 <= s.length <= 100
    s[i] is '(', ')' or '*'.

"""
class Solution:
    def checkValidString(self, s: str) -> bool:
        dp = { (len(s), 0) : True }
        def dfs(i, count):
            if i == len(s):
                return count ==0
            if count<0:
                return False
            if (i,count) in dp:
                return dp[(i,count)]
            
            if s[i]=="*":
                dp[(i,count)] = dfs(i+1, count+1) or dfs(i+1,count) or dfs(i+1, count-1)
            elif s[i]=="(":
                dp[(i,count)] = dfs(i+1,count+1)
            else:
                dp[(i,count)] = dfs(i+1, count-1)
            
            return dp[(i,count)]
        return dfs(0,0)
# class Solution:
#     def checkValidString(self, s: str) -> bool:
#         leftMin,leftMax =0,0
        
#         for c in s:
#             if c =="(":
#                 leftMin,leftMax =leftMin+1,leftMax+1
#             elif c ==")":
#                 leftMin,leftMax =leftMin-1,leftMax-1
#             else:
#                 leftMin,leftMax =leftMin-1,leftMax+1
            
#             if leftMax<0:
#                 return False
#             if leftMin<0:
#                 leftMin = 0
        
#         return leftMin==0