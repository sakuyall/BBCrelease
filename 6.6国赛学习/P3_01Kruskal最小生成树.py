"""5/21/26
其中直接包含了find及union函数, 这是并查集的基本函数方法
Kruskal算法适用于小范围图的最小生成树
其中并查集部分基本是原封不动的
"""
import sys, os
from io import StringIO
sys.setrecursionlimit(100000)
'''
data = "\
4 5\n\
1 2 1\n\
1 3 2\n\
1 4 3\n\
2 3 2\n\
3 4 4"
sys.stdin = StringIO(data)
'''
def find(x):
    if x != father[x]:
        root = find(father[x])
        father[x] = root
    return father[x]

def union(x, y):
    x, y = find(x), find(y)
    if x != y:
        # 未建立连接则建立并返回建立成功
        father[x] = y
        return True
    # 已有联系无需建立
    return False

n, m = map(int, input().split())
ans, cnt = 0, 0
father = list(range(n + 1))
edges = []

for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

edges.sort()

for w, u, v in edges:
    if union(u, v):
        ans += w    # 边权累计
        cnt += 1    # 边数记录
        if cnt == n - 1:
            # 到达n - 1条边提前跳出循环
            break

if cnt == n - 1:
    # 输出边权值
    print(ans)
else:
    # 循环结束未达到要求则返回不可能建立
    print("impossible")
