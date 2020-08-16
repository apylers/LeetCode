from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, newColor: int
    ) -> List[List[int]]:
        anchor = image[sr][sc]  # 原颜色
        if anchor == newColor:
            # 原颜色与新颜色相同，图片不变
            return image

        row_len, column_len = len(image), len(image[0])  # 图片高宽
        sides = ((0, -1), (0, 1), (-1, 0), (1, 0))  # 四周移动

        remain_points = [(sr, sc)]  # 以初始点开始深度优先
        while remain_points:
            row, column = remain_points.pop()
            image[row][column] = newColor  # 涂成新颜色
            # 检查四周，不越界且为原颜色的加入栈
            for row_para, column_para in sides:
                new_row, new_column = row + row_para, column + column_para
                if (
                    0 <= new_row < row_len
                    and 0 <= new_column < column_len
                    and image[new_row][new_column] == anchor
                ):
                    remain_points.append((new_row, new_column))

        return image


image = [[0, 0, 0], [0, 1, 1]]
sr = 1
sc = 1
newColor = 1
image = Solution().floodFill(image, sr, sc, newColor)
print(image)
