"""5/19/26
内容上来说不是很难, 参考b视频思路
"""
import sys, os
sys.setrecursionlimit(100000)

# 查找根节点
def find(x):
    if x == father[x]:
        # 根节点返回自身
        return x
    # 优化, 将根节点直接设为节点x的父节点, 防止递归深度过大
    father[x] = find(father[x])

    return father[x]

# 集合合并
def union(x, y):
    # 判断是否已经处于同一集合
    a = find(x)
    b = find(y)
    if a == b:
        # 处于同一集合不进行操作
        return
    # 谁是父节点无所谓的, 只要是建立联系了就可以
    father[a] = b

n, m = map(int, input().split())
father = list(range(n+1))    # 初始化默认全部为根节点(父节点是本身)

for _ in range(m):
    tp, a, b = input().strip().split()
    a, b = int(a), int(b)

    if tp == "M":
        union(a, b)
    else:
        if find(a) == find(b):
            print("Yes")
        else:
            print("No")
