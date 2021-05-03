from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        wait = [0]  # 起始点进栈
        finished = set()  # 已进入房间
        while wait:
            room = wait.pop()
            finished.add(room)
            wait += rooms[room]  # 拿到新房间钥匙
            rooms[room] = []  # 当前房间钥匙清空
        return len(finished) == len(rooms)  # 已进入房间数等于总数


rooms = [[1, 3], [3, 0, 1], [2], [0]]
result = Solution().canVisitAllRooms(rooms)
print(result)
