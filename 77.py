from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(start, k):
            """从 start 开始的 k 个数的组合"""

            if k == 1:
                # 单一数，直接返回
                return [[i] for i in range(start, n + 1)]

            results = []
            for i in range(start, n + 2 - k):
                # 从 start 开始，到 n + 1 - k 结束（从 n + 2 - k 开始凑不满 k 个数，直接舍去）
                remain = dfs(i + 1, k - 1)  # 获取子列
                result = [[i] + j for j in remain]  # 添加当前数
                results += result  # 合并至结果

            return results

        return dfs(1, k)


n = 4
k = 2
result = Solution().combine(n, k)
print(result)
