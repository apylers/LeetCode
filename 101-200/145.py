from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def dfs(root):
            if not root:
                # 无节点，直接返回
                return
            dfs(root.left)  # 左
            dfs(root.right)  # 右
            result.append(root.val)  # 中

        result = list()
        dfs(root)
        return result
