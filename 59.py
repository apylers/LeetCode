from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0] * n for _ in range(n)]
        direction = 0
        i, j = 0, 0
        result[0][0] = 1
        item = 2
        while item <= n ** 2:
            if direction == 0:
                if j + 1 < n and result[i][j + 1] == 0:
                    j += 1
                    result[i][j] = item
                    item += 1
                    continue
                else:
                    direction = 1
            if direction == 1:
                if i + 1 < n and result[i + 1][j] == 0:
                    i += 1
                    result[i][j] = item
                    item += 1
                    continue
                else:
                    direction = 2
            if direction == 2:
                if j - 1 >= 0 and result[i][j - 1] == 0:
                    j -= 1
                    result[i][j] = item
                    item += 1
                    continue
                else:
                    direction = 3
            if direction == 3:
                if i - 1 >= 0 and result[i - 1][j] == 0:
                    i -= 1
                    result[i][j] = item
                    item += 1
                else:
                    direction = 0
        return result


n = 10
result = Solution().generateMatrix(n)
print(result)
