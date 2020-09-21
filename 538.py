# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            if not root:
                # 节点不存在，直接返回
                return

            nonlocal temp
            dfs(root.right)  # 处理右侧
            root.val += temp  # 修改值
            temp = root.val  # 修改 temp
            dfs(root.left)  # 处理左侧

        temp = 0
        dfs(root)

        return root
