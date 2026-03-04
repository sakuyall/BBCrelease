"""3/4/26
在序列中若出现不满足条件情况则会使原序列出现断点
所以下一次寻找可以直接从断点后再开始寻找
i..........
i...j......
....ji.....
.....i.....
.....ij....
"""
n = int(input())
li = list(map(int, input().split()))

res = []
length = 1
i, j = 0, 0
if len(li) < 2:
    res.append(length)    # 序列长度为1
while j + 1 <= n - 1:     # 右指针防止超过右边界
    if li[j] * 2 >= li[j + 1]:
        # 满足条件时
        j += 1
        length += 1
    else:
        # 不满足条件时
        if j + 1 <= n - 1:    # 右指针防止超过右边界
            i, j = j + 1, i
        res.append(length)
        length = 1            # 重置长度为1

res.append(length)    # 防止最后一个数值未被记录
print(max(res))