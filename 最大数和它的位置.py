"""
列表加索引方法
"""
li = []
for _ in range(100):
    li.append(int(input()))   # 循环100次把每行输入加入列表
m = max(li)
ans = li.index(m) + 1         # 列表从0开始, 题目要求从1开始
print(m, ans, sep = "\n")     # 分开写两个print也行

"""
边读边取方法
"""
max_value = -1
max_index = -1
for _ in range(1, 101):       # 直接从1开始记录
    n = int(input())
    if n > max_value:         # 有新的大值
        max_value = n         # 赋予新的数与位置
        max_index = _

print(max_value, max_index, sep = "\n")