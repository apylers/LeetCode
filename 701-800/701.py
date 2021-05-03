# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        new = TreeNode(val)  # 新建节点

        if not root:
            # 无根节点，返回新节点
            return new

        current = root
        while True:
            if current.val > val:
                # 左侧找
                if current.left:
                    current = current.left
                else:
                    current.left = new
                    return root
            else:
                # 右侧找
                if current.right:
                    current = current.right
                else:
                    current.right = new
                    return root
