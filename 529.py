from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        start_row, start_column = click
        if board[start_row][start_column] == "M":
            # 起始点为地雷，直接修改为 X 后返回即可
            board[start_row][start_column] = "X"
            return board

        stack = [(start_row, start_column)]  # 起始点进栈
        while stack:
            # 循环至栈为空
            row, column = stack.pop()
            board[row][column] = "B"  # 暂时将此处设为 B
            temp = []  # 临时储存八个方向中可继续延伸的点
            M_count = 0  # 记录八个方向中地雷的个数
            for i in range(-1, 2):
                if not 0 <= row + i < len(board):
                    # 行下标防止越界
                    continue
                for j in range(-1, 2):
                    if not 0 <= column + j < len(board[0]):
                        # 纵下标防止越界
                        continue
                    if board[row + i][column + j] == "M":
                        # 周围有地雷，地雷数 + 1
                        M_count += 1
                    elif board[row + i][column + j] == "E":
                        # 周围也为空，临时储存起来
                        temp.append((row + i, column + j))
                    # 为 B 或数字时直接跳过
            if M_count:
                # 有地雷，修改为对应数值
                board[row][column] = str(M_count)
            else:
                # 否则 temp 进栈
                stack += temp
        return board


board = [
    ["E", "E", "E", "E", "E"],
    ["E", "E", "M", "E", "E"],
    ["E", "E", "E", "E", "E"],
    ["E", "E", "E", "E", "E"],
]
click = [3, 0]
result = Solution().updateBoard(board, click)
print(result)
