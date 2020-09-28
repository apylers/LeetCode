from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: "Node" = None, right: "Node" = None, next: "Node" = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Node") -> "Node":
        queue = deque()

        queue.append(root)  # 初始化队列
        queue.append(None)  # 层结束标志

        before = None  # 待更新 next，None 代表换层

        while queue:
            current = queue.popleft()  # 出队

            if not current:
                # 层结束
                if not before:
                    # 表示该层没节点，即已完成整棵树遍历
                    return root

                before = None  # 清空 before
                queue.append(None)  # 添加层结束标志
                continue

            # 左右子节点依次进队
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

            if before:
                # 当前不是该层第一个，则更新 next
                before.next = current

            before = current
