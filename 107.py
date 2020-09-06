from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            # 无根节点，返回空
            return []

        q = deque()  # 新建队列
        q.append(root)  # 根节点入队
        result = []  # 逆序储存结果

        while q:
            temp_result = []  # 保存每一行的结果
            count = len(q)  # 获取当前队列长度
            for _ in range(count):
                node = q.popleft()  # 出队
                temp_result.append(node.val)
                # 存在左右子节点，则入队
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(temp_result)

        return result[::-1]
