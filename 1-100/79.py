from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(pos, word):
            if not word:
                # 字符用完，则已找出
                return True

            row, column = pos
            for i, j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                # 四个方向
                if row + i < 0 or row + i >= len(board) or column + j < 0 or column + j >= len(board[0]):
                    # 越界则跳过
                    continue

                if board[row + i][column + j] == word[0]:
                    board[row + i][column + j] = "1"  # 做标记
                    if dfs((row + i, column + j), word[1:]):
                        # 子列也找得到，返回真
                        return True
                    # 子列找不到，回溯原来的值
                    board[row + i][column + j] = word[0]

            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                # 寻找起始点
                if board[i][j] == word[0]:
                    board[i][j] = "1"  # 做标记
                    if dfs((i, j), word[1:]):
                        # 子列也找得到，返回真
                        return True
                    # 子列找不到，回溯原来的值
                    board[i][j] = word[0]

        return False


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "CBFDEES"
result = Solution().exist(board, word)
print(result)
