class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
            
        val = tokens.pop()
        
        if val.lstrip("-").isdigit():
            return int(val)
        
        if val == "+":
            rhs = self.evalRPN(tokens)
            lhs = self.evalRPN(tokens)
            return lhs + rhs
        elif val == "-":
            rhs = self.evalRPN(tokens)
            lhs = self.evalRPN(tokens)
            return lhs - rhs
        elif val == "*":
            rhs = self.evalRPN(tokens)
            lhs = self.evalRPN(tokens)
            return lhs * rhs
        elif val == "/":
            rhs = self.evalRPN(tokens)
            lhs = self.evalRPN(tokens)
            return int(lhs / rhs)