"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def dfs(self, node):
        if node in self.oldToNew:
            return self.oldToNew[node]
        
        copy=Node(node.val)
        self.oldToNew[node]=copy

        for nei in node.neighbors:
            copy.neighbors.append(self.dfs(nei))
        
        return copy
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        self.oldToNew={}
        copy=self.dfs(node)
        return copy

        