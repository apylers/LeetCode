from typing import List


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        def dp(i, j, k):
            if i > j:
                # 下标左高于右，直接返回 0
                return 0
            if dp_table[i][j][k] != 0:
                # dp_table 已经有值，返回
                return dp_table[i][j][k]

            dp_table[i][j][k] = dp(i, j - 1, 0) + (k + 1) ** 2  # 默认处理方式，将后方所有重复元素直接兑换分数
            for j_pre in range(i, j):
                if boxes[j_pre] == boxes[j]:
                    # 在 i 和 j 之间搜索与 boxes[j] 相同的元素
                    # 分数计算为兑换 j_pre + 1 ~ j - 1 的分数与剩余部分的分数之和
                    dp_table[i][j][k] = max(
                        dp_table[i][j][k], dp(i, j_pre, k + 1) + dp(j_pre + 1, j - 1, 0)
                    )

            return dp_table[i][j][k]

        dp_table = [[[0] * 100 for _ in range(100)] for _ in range(100)]  # 存储表
        return dp(0, len(boxes) - 1, 0)


boxes = [6, 3, 6, 5, 6, 6, 6]
result = Solution().removeBoxes(boxes)
print(result)
