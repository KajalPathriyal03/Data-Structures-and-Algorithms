from sortedcontainers import SortedList
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        self.levels = {}
        self.heights = {}
        self.firstMax = collections.defaultdict(int)
        self.secMax = collections.defaultdict(int)

        self.find_heights(root, 0)

        results = []
        for node in queries:
            node_level = self.levels[node]
       
            if self.firstMax[node_level] == self.heights[node]:
                maxH = self.secMax[node_level]
            else:
                maxH = self.firstMax[node_level]

            new_height = node_level + maxH - 1
            results.append(new_height)

        return results

    def find_heights(self, root: TreeNode, level: int) -> int:
        if not root:
            return 0

        left_height = self.find_heights(root.left, level + 1)
        right_height = self.find_heights(root.right, level + 1)
        
        height = max(left_height, right_height) + 1

        self.levels[root.val] = level
        self.heights[root.val] = height

        # Update the max and second max heights for the current level
        if height > self.firstMax[level]:
            self.secMax[level] = self.firstMax[level]
            self.firstMax[level] = height
        elif height > self.secMax[level]:
            self.secMax[level] = height

        return height