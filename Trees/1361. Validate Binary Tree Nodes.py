"""
You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.

If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

Note that the nodes have no values and that we only use the node numbers in this problem.

 

Example 1:

Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
Output: true

Example 2:

Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
Output: false

Example 3:

Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
Output: false

 

Constraints:

    n == leftChild.length == rightChild.length
    1 <= n <= 104
    -1 <= leftChild[i], rightChild[i] <= n - 1
"""
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        l_set = set(leftChild)
        r_set = set(rightChild)
        union_lr_set = l_set.union(r_set)
        full_set = set([i for i in range(n)])
        root_set = full_set.difference(union_lr_set)
        
        if len(root_set) > 1 or len(root_set) ==0:
            return False
        
        visited = set()
        
        q = deque([root_set.pop()])
        
        while q:
            node = q.popleft()
            if node in visited:
                return False
            
            visited.add(node)
            if leftChild[node] != -1:
                q.append(leftChild[node])
            
            if rightChild[node] != -1:
                q.append(rightChild[node])
            
        return len(visited) == n