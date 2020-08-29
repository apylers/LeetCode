class Solution:
    def shortestPalindrome(self, s: str) -> str:
        s_rev = s[::-1]  # 反向
        for i in range(len(s), 0, -1):
            # 逐个比较直至出现相同
            if s[:i] == s_rev[len(s) - i :]:
                return s_rev[: len(s) - i] + s
        return ""


s = ""
result = Solution().shortestPalindrome(s)
print(result)
