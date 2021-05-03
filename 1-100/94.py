from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def dfs(root):
            if not root:
                return

            dfs(root.left)  # 左
            series.append(root.val)  # 中
            dfs(root.right)  # 右

        series = list()
        dfs(root)

        return series
