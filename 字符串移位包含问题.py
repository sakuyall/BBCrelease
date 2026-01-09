"""1/9/26
判断短的是否为长的移位后的字串, 比较两者长度分别讨论
也不去管麻烦的移位, 原字符串复制拼接来解决边界问题
判断第二个字符串在不在那个里就行
"""
s1, s2 = map(str, input().split())
ss1, ss2= len(s1), len(s2)

if ss1 == ss2:
    if s2 in s1 * 2:          # 长度相同的拼接
        print("true")
    else:
        print("false")
    
if ss1 > ss2:
    if s2 in s1 * 2:
        print("true")
    else:
        print("false")
        
if ss2 > ss1:
    if s1 in s2 * 2:
        print("true")
    else:
        print("false")

# 简化版
s1, s2 = input().split()
if len(s1) > len(s2): s1, s2 = s2, s1
print('true' if s1 in s2 * 2 else 'false')