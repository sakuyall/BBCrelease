"""2/1/26
扩散过程, 扩散距离初始点曼哈顿距离为0, 1, 2这样变化
形成连通块, 两个初始点扩散有公共点, 也就是有一个点同时满足所有这两个条件
对于给定范围, t越大越容易连通
"""
def md(a, b, x, y):
    aa = abs(x - a)
    bb = abs(y - b)
    return int(aa + bb)

def count(li, t):
    """判断在时刻t时所有点是否连通"""
    n = len(li)
    
    # 构建连通关系图
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            distance = md(li[i][0], li[i][1], li[j][0], li[j][1])
            if distance <= 2 * t:  # 在时刻t两点扩散区域有重叠
                graph[i].append(j)
                graph[j].append(i)
    
    # 如果只有一个点，总是连通的
    if n <= 1:
        return True
    
    # 使用BFS检查所有点是否连通
    visited = [False] * n
    stack = [0]
    visited[0] = True
    visited_count = 1
    
    while stack:
        node = stack.pop()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)
                visited_count += 1
    
    # 如果访问了所有点，说明整个图是连通的
    return visited_count == n

# 主程序
n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]

# 二分查找最小连通时间
left, right = 0, 1000000000
while left <= right:
    mid = (left + right) // 2
    if count(li, mid):
        right = mid - 1  # 如果mid时刻能连通，尝试更小的时间
    else:
        left = mid + 1   # 如果mid时刻不能连通，需要更大的时间

# 最终left是最小满足条件的时间
print(left)