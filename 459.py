class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for repeat in range(1, len(s) // 2 + 1):
            # repeat 为重复字符串长度

            if len(s) // repeat * repeat != len(s):
                # 如果不能整除 s 总长度，舍弃
                continue

            for i in range(repeat, len(s)):
                if s[i] != s[i % repeat]:
                    break
            else:
                # 未出现 break，说明可行
                return True

        # 每种长度都不可行
        return False


s = "abcabcabcabc"
result = Solution().repeatedSubstringPattern(s)
print(result)
