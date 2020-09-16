# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            if not root:
                # 无节点，直接返回
                return

            root.left, root.right = root.right, root.left  # 左右交换
            dfs(root.left)  # 左侧全交换
            dfs(root.right)  # 右侧全交换

        dfs(root)
        return root
