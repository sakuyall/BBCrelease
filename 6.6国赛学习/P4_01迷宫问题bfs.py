"""5/26/26
这是迷宫问题的bfs写法
理解了思路后独立完成一次
发现bfs不需要像dfs一样传入参数以及锚定当前状态
在听了随想录课程后有了一定的启发, 今日已完成
dfs与bfs模板题目学习
"""
import sys, os
from io import StringIO
from collections import deque

def bfs():
    if martix[x2][y2] == 0:
        # 出口为障碍特判
        print(-1)
        return
    
    while q:
        # 双端队列左出右进
        x, y = q.popleft()
        for i in range(4):
            # 四方向判断, 为障碍物则跳过
            new_x, new_y = x + dx[i], y + dy[i]
            if 1 <= new_x <= n and 1 <= new_y <= m:
                # 不越界情况下
                if martix[new_x][new_y] == 1 and dis[new_x][new_y] == -1:
                    # 该位置为通路且未遍历过
                    dis[new_x][new_y] = dis[x][y] + 1# 该位置步数为上一位置加1
                    q.append((new_x, new_y))    # 满足以上条件将其入队
    
    # 最终队空可以得出答案
    if dis[x2][y2] == -1:
        print(-1)
        return
    else:
        print(dis[x2][y2])
        return

n, m = map(int, input().split())
# 为与输入的起点终点坐标相匹配, 所以加入空行空列
martix = [[0] * (m + 1)]
for _ in range(n):
    martix.append([0] + list(map(int, input().split())))

# 读取起点终点
x1, y1, x2, y2 = map(int, input().split())
# 初始化距离矩阵, -1设置为未遍历过
dis = [[-1] * (m + 1) for _ in range(n + 1)]
dis[x1][y1] = 0    # 起点距离设为0

# 建立双端队列, 放入起点
q = deque()
q.append((x1, y1))

# 位置变化量 右 左 下 上
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

bfs()
