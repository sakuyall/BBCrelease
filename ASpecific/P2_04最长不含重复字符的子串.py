"""3/6/26
这题要求只定义函数, 但完整版本都放这里了
知识点: 滑动窗口
"""
s = str(input()).strip('"')      # 假如输入就长这样, 要去掉输入两侧的多余引号
length = len(s)

if length == 0:
    print(0)
else:
    i, j = 0, 0
    maxlen = 1
    li = [0] * 26                # 使用0至25序号
    li[ord(s[i]) - ord("a")] = 1 # 标记i位置字符已使用

    while j < length - 1:    # j指向下一个待查找字符
        # 尝试拓展窗口
        next_char = s[j + 1]
        next_index = ord(next_char) - ord("a")

        if li[next_index] == 0:
            # 执行向右拓展窗口
            j += 1
            li[next_index] = 1
            current_len = j - i + 1
            maxlen = max(maxlen, current_len)
        else:
            # 右边不动, 左边收缩
            # 并移除左边i位置字符的标记
            li[ord(s[i]) - ord("a")] = 0
            i += 1
    print(maxlen)

# 题目AC版本应该是这样的--------------------------------------------------------------
class Solution:
    def longestSubstringWithoutDuplication(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)

        if length == 0:
            return 0
        else:
            i, j = 0, 0
            maxlen = 1
            li = [0] * 26                # 使用0至25序号
            li[ord(s[i]) - ord("a")] = 1 # 标记i位置字符已使用

            while j < length - 1:    # j指向下一个待查找字符
                # 尝试拓展窗口
                next_char = s[j + 1]
                next_index = ord(next_char) - ord("a")

                if li[next_index] == 0:
                    # 执行向右拓展窗口
                    j += 1
                    li[next_index] = 1
                    current_len = j - i + 1
                    maxlen = max(maxlen, current_len)
                else:
                    # 右边不动, 左边收缩
                    # 并移除左边i位置字符的标记
                    li[ord(s[i]) - ord("a")] = 0
                    i += 1

        return maxlen