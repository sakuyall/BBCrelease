"""3/2/26"""
# 导入bisect查找第一个大于等于该数的位置
import bisect

n, m = map(int, input().split())
li = list(map(int, input().split()))
que = list(map(int, input().split()))

ans = []
for target in que:
    pos = bisect.bisect_left(li, target)
    # 同时确保不越界且在列表内, 注意先检查越界再访问元素
    if pos < n and li[pos] == target:
        # 注意位置从1开始编号, 索引应加1
        ans.append(pos+1)
    else:
        ans.append(-1)

print(*ans)