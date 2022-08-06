"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []
        open_pc = 0
        close_pc = 0
        def backtrack():
            nonlocal open_pc, close_pc
            if open_pc == close_pc == n:
                result.append("".join(stack))
                return
            
            if open_pc < n:
                stack.append("(")
                open_pc += 1
                backtrack()
                stack.pop()
                open_pc -= 1
            
            if close_pc < open_pc:
                close_pc += 1
                stack.append(")")
                backtrack()
                stack.pop()
                close_pc -= 1
        
        backtrack()
        return result