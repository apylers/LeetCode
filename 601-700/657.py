from collections import defaultdict


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        move_dict = defaultdict(lambda: 0)  # 新建字典，默认取值为 0

        # 对每个方向计数
        for move in moves:
            move_dict[move] += 1

        # 上下、左右对应相等
        return move_dict["U"] == move_dict["D"] and move_dict["L"] == move_dict["R"]


moves = "ULLUUDRDRD"
result = Solution().judgeCircle(moves)
print(result)
