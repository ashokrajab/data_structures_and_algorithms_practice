"""
You are given a tree with n nodes numbered from 0 to n - 1 in the form of a parent array parent where parent[i] is the parent of ith node. The root of the tree is node 0. Find the kth ancestor of a given node.

The kth ancestor of a tree node is the kth node in the path from that node to the root node.

Implement the TreeAncestor class:

    TreeAncestor(int n, int[] parent) Initializes the object with the number of nodes in the tree and the parent array.
    int getKthAncestor(int node, int k) return the kth ancestor of the given node node. If there is no such ancestor, return -1.

 

Example 1:

Input
["TreeAncestor", "getKthAncestor", "getKthAncestor", "getKthAncestor"]
[[7, [-1, 0, 0, 1, 1, 2, 2]], [3, 1], [5, 2], [6, 3]]
Output
[null, 1, 0, -1]

Explanation
TreeAncestor treeAncestor = new TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2]);
treeAncestor.getKthAncestor(3, 1); // returns 1 which is the parent of 3
treeAncestor.getKthAncestor(5, 2); // returns 0 which is the grandparent of 5
treeAncestor.getKthAncestor(6, 3); // returns -1 because there is no such ancestor

 

Constraints:

    1 <= k <= n <= 5 * 104
    parent.length == n
    parent[0] == -1
    0 <= parent[i] < n for all 0 < i < n
    0 <= node < n
    There will be at most 5 * 104 queries.

"""
class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.ancestor =[parent]
        self.max_stride = len(format(n, "b"))
        
        for i in range(1, self.max_stride):
            gen_i_of_node_j = []
            for j in range(n):
                val = -1
                if self.ancestor[i-1][j] != -1:
                    val = self.ancestor[ i-1 ][ self.ancestor[i-1][j] ]
                gen_i_of_node_j.append(val)
            self.ancestor.append(gen_i_of_node_j)
            
    def getKthAncestor(self, node: int, k: int) -> int:
        k_binary = list(format(k, "b"))
        position = len(k_binary)
        if self.max_stride < position:
            return -1
        
        for bit in k_binary:
            if node == -1:
                return -1
            position -= 1
            if bit == '0':
                continue
            node = self.ancestor[position][node]
        return node


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)