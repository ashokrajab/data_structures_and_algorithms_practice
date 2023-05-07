"""
Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.

 

Example 1:

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4),
pop() -> 4,
push(5),
pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
Example 2:

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.
 

Constraints:

1 <= pushed.length <= 1000
0 <= pushed[i] <= 1000
All the elements of pushed are unique.
popped.length == pushed.length
popped is a permutation of pushed.
"""
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pushed_map = {val:idx for idx,val in enumerate(pushed)}
        idx = pushed_map[popped[0]]
        
        stack = []
        for i in range(idx):
            stack.append(pushed[i])

        prev_idx = idx
        for k in range(1, len(popped)):
            curr_idx = pushed_map[popped[k]]
            if curr_idx > prev_idx:
                for l in range(prev_idx+1, curr_idx):
                    stack.append(pushed[l])
                prev_idx = curr_idx
            else:
                curr_val = popped[k]
                if not stack or curr_val != stack[-1]:
                    return False
                else:
                    stack.pop()
        return True
            