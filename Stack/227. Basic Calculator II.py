"""
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "3+2*2"
Output: 7

Example 2:

Input: s = " 3/2 "
Output: 1

Example 3:

Input: s = " 3+5 / 2 "
Output: 5

 

Constraints:

    1 <= s.length <= 3 * 105
    s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
    s represents a valid expression.
    All the integers in the expression are non-negative integers in the range [0, 231 - 1].
    The answer is guaranteed to fit in a 32-bit integer.

"""
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def operate(o1, o2, op):
            match op:
                case "+": return o1 + o2
                case "-": return o1 - o2
                case "*": return o1 * o2
                case "/": return o1 // o2
                
        ops = []
        nums = []
        s_len = len(s)
        precedence = {"/":2, "*":2, "+":1, "-":1}
        i = 0
        while i < s_len:
            c = s[i]
            if c == " ":
                i += 1
                continue
            if c.isdigit():
                curr_num = 0
                while i < s_len and s[i].isdigit():
                    curr_num = curr_num*10 + int(s[i])
                    i += 1
                nums.append(curr_num)
                i -= 1
            else:
                while ops and precedence[c] <= precedence[ops[-1]]:
                    operand_2, operand_1 = nums.pop(), nums.pop()
                    operator = ops.pop()
                    ans = operate(operand_1, operand_2, operator)
                    nums.append(ans)
                
                ops.append(c)
            i += 1
        
        while ops:
            operand_2, operand_1 = nums.pop(), nums.pop()
            operator = ops.pop()
            ans = operate(operand_1, operand_2, operator)
            nums.append(ans)
        
        return nums[-1]
            
            