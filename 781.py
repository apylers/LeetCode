from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers_dict = {}
        for answer in answers:
            answers_dict[answer] = answers_dict.get(answer, 0) + 1

        amount = 0
        for key, value in answers_dict.items():
            amount += (key + 1) * ((value + key) // (key + 1))

        return amount


answers = [0, 0, 1, 1, 1]
result = Solution().numRabbits(answers)
print(result)
