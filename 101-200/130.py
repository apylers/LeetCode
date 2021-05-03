from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 无数据直接 return
        if not board:
            return

        rows, columns = len(board), len(board[0])
        collect_board = list()  # 标记确定留下的 O
        remain_board = list()  # 剩余未确定的 O

        for row in range(rows):
            for column in range(columns):
                if board[row][column] == "O":
                    if row in (0, rows - 1) or column in (0, columns - 1):
                        # 在四周的一定会留下
                        collect_board.append((row, column))
                    else:
                        # 其余放入不确定列表
                        remain_board.append((row, column))

        # print(collect_board)
        # print(remain_board)

        # 对确定留下的 O 四面考察，看是否存在其他的 O，若存在，则将其从 remain_board 移入 collect_board
        i = 0
        while i < len(collect_board):
            row, column = collect_board[i]
            for position in (
                (row + 1, column),
                (row - 1, column),
                (row, column + 1),
                (row, column - 1),
            ):
                try:
                    collect_board.append(remain_board.pop(remain_board.index(position)))
                except Exception:
                    continue
            i += 1

        # print(collect_board)
        # print(remain_board)

        # 最后仍在不确定列表中的 O 都没有与最外层的 O 相连，填充成 X
        for row, column in remain_board:
            board[row][column] = "X"


board = [
    ["X", "X", "X", "X", "X"],
    ["X", "O", "O", "O", "O"],
    ["X", "X", "X", "O", "X"],
    ["X", "O", "X", "O", "X"],
    ["X", "X", "X", "X", "X"],
]
Solution().solve(board)
print(board)
