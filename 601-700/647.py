class Solution:
    def countSubstrings(self, s: str) -> int:
        s_len = len(s)  # 总长
        result = s_len  # 每个字符都是一个回文串

        # 单字符中心
        for i in range(1, s_len - 1):
            for j in range(1, min(i + 1, s_len - i)):  # 确定可扩展的最大范围
                # 以 s[i] 为中心
                if s[i - j] != s[i + j]:
                    # 对称位置字符不同，不再扩展
                    break
                result += 1

        # 双字符中心
        for i in range(0, s_len - 1):
            if s[i] != s[i + 1]:
                # 字符不同，跳过
                continue
            result += 1
            for j in range(1, min(i + 1, s_len - i - 1)):  # 确定可扩展的最大范围
                # 以 s[i], s[i + 1] 为中心
                if s[i - j] != s[i + j + 1]:
                    # 对称位置字符不同，不再扩展
                    break
                result += 1

        return result


s = "abaaaabaa"
result = Solution().countSubstrings(s)
print(result)
