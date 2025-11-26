"""11/26/25
兰顿蚂蚁
    ----
分析
    输入:m n表示行数和列数
        m行数据,每行为n个空格分隔的数,0白黑1
        x y s r表示 行号, 列号(0开始), 初始朝向(上下左右UDLR), 行走步数
    输出:
        p q行走k步后所在位置 行号和列号
总结
    借助了一些deepseek
"""
def toward(x, y, s):  # 添加坐标参数
    """
    黑格右转+1,白格左转-1
       U
    L     R
       D
    """
    tow = ['U', 'R', 'D', 'L']
    position = tow.index(s)              # 获取当前方向在tow里的位置
    if square[x][y] == 1:
        # 处于黑格右转+1
        position = (position + 1) % 4    # 在列表内循环方向
    else:
        # 处于白格左转-1
        position = (position - 1) % 4
    return tow[position]                 # 返回转向后朝向

def step(x, y, s):
    # 设定上下左右移动后xy变化
    if s == "U":
        x -= 1
    elif s == "D":
        x += 1
    elif s == "L":
        y -= 1
    elif s == "R":
        y += 1
    return x, y

# 蚂蚁初始落地后直接根据地面颜色转向,然后再移动
def move(x, y, s, k):
    while k > 0:
        s = toward(x, y, s)              # 传递坐标参数,获取新朝向
        square[x][y] = 1 - square[x][y]  # 变更地面颜色 
        x, y = step(x, y, s)             # 移动一步
        k -= 1                           # 步数减一
    return x, y  # 返回坐标

m, n = map(int, input().split())         # 传入mn
square = []
for _ in range(m):                       # 传入二维列表
    square.append(list(map(int, input().split())))

x, y, s, k = input().split()             # 传四个值
x, y, k = int(x), int(y), int(k)

final_x, final_y = move(x, y, s, k)

# 输出结果
print(final_x, final_y)