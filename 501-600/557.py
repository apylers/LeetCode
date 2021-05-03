class Solution:
    def reverseWords(self, s: str) -> str:
        # 反转，分割，再反转，合并
        return " ".join(s[::-1].split()[::-1])


s = "Let's take LeetCode contest"
result = Solution().reverseWords(s)
print(result)
