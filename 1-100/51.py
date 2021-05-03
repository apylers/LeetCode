from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(rows):
            """
            :param rows: 求前 rows 行所有可行情况
            :return: 前 rows 行所有可行情况
            """
            if rows == 1:
                # 初始行，每个点都可行
                return [[i] for i in range(n)]

            prev = dfs(rows - 1)  # 先求出前 rows - 1 行所有可行情况
            curr = []  # 储存前 rows 行所有可行情况

            for pos in prev:
                # pos: 前 rows - 1 行某一可行情况
                choices = list(range(n))  # 新增行可能情况候选
                for index, i in enumerate(pos[::-1]):
                    # index: i 所在行与新增行的距离
                    # 删除同列和对角的情况
                    try:
                        choices.remove(i)
                    except:
                        pass
                    try:
                        choices.remove(i + index + 1)
                    except:
                        pass
                    try:
                        choices.remove(i - index - 1)
                    except:
                        pass

                for choice in choices:
                    # 剩下的情况为可行情况
                    curr.append(pos + [choice])
            return curr

        total = dfs(n)

        # 绘制棋盘
        boards = []
        for ready in total:
            board = []
            for row in ready:
                temp = ["."] * n
                temp[row] = "Q"
                board.append("".join(temp))
            boards.append(board)

        return boards


n = 4
result = Solution().solveNQueens(n)
print(result)
