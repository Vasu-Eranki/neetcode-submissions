"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hashset = {}
        def dfs(node):
            if not node:
                return 
            if node in hashset:
                return hashset[node]
            new_node = Node(node.val)
            hashset[node] = new_node
            if node.neighbors:
                new_neighbors = []
                for neighbour in node.neighbors:
                    new_neighbour = dfs(neighbour)
                    new_neighbors.append(new_neighbour)
                new_node.neighbors = new_neighbors
            return new_node
        return dfs(node)

        