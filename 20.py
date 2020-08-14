class Solution:
    def isValid(self, s: str) -> bool:
        pair = {"}": "{", "]": "[", ")": "("}  # 匹配字典
        stack = []  # 栈
        for c in s:
            if c in pair:
                # c 为反括号
                try:
                    c_pair = stack.pop()
                    if pair[c] != c_pair:
                        # 没有正括号与 c 匹配
                        return False
                except:
                    # stack 为空
                    return False
            else:
                # 正括号进栈
                stack.append(c)
        return not stack  # 最后应该栈空


s = "{()[{()}]}"
result = Solution().isValid(s)
print(result)
