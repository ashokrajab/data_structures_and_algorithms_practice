from collections import deque
from typing import Optional
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append((root,0))
        ans = 1
        while q:
            q_len = len(q)
            l,r=None, None
            for i in range(q_len):
                node, idx = q.popleft()
                if l == None:
                    l = idx
                else:
                    r = idx
                if node.left:
                    q.append((node.left, 2*idx + 1))
                if node.right:
                    q.append((node.right, 2*idx + 2))
                    
            if l is not None and r is not None:
                ans = max(ans, r-l+1)
        return ans
Solution().widthOfBinaryTree(root=root) 