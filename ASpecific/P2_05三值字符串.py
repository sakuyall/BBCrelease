"""3/7/26
难, 最后需要检查收缩
知识点: 滑动窗口
"""
def calculate(s):
    length = len(s)

    if length == 0 or set(s) != {"1", "2", "3"}:
        # 若字符串不包含123任意一个
        return 0
    
    i, j = 0, 0
    minlen = 200000        # 设置较大初值
    hax = [0, 0, 0]        # 统计123出现次数
    hax[int(s[i]) - 1] = 1 # i位置标记1次
        
    while j < length - 1:
        # 尝试扩充窗口
        next_char = s[j + 1]
        next_index = int(next_char) - 1

        while 0 not in hax:
            # 满足条件持续收缩
            hax[int(s[i]) - 1] -= 1     # 左窗口排出
            minlen = min(minlen, j - i + 1)
            i += 1                      # 左缩

            
        # 若仍缺少123中的某一个
        # 向右扩充
        j += 1                      # 右扩
        hax[next_index] += 1        # 次数加1
        if 0 not in hax:
            # 若此时已经满足条件, 则储存最小值
            minlen = min(minlen, j - i + 1)
                    
    # 循环结束后检查最后一次形成的窗口
    while 0 not in hax:
        minlen = min(minlen, j - i + 1)
        hax[int(s[i]) - 1] -= 1    # 持续收缩窗口至不满足条件
        i += 1

    return minlen

t = int(input())
for _ in range(t):
    s = str(input())
    print(calculate(s))