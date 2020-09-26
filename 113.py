from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def dfs(root, remain, prefix):
            remain -= root.val  # 添加 root 对应值

            if (not root.left) and (not root.right):
                # root 为叶子
                if remain == 0:
                    result.append(prefix + [root.val])
                return

            if root.left:
                dfs(root.left, remain, prefix + [root.val])
            if root.right:
                dfs(root.right, remain, prefix + [root.val])

        result = []

        if root:
            # 树存在才执行
            dfs(root, sum, [])

        return result
