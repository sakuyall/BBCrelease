"""11/28/25
螺旋折线
    ----数学题 找规律
    输入坐标x y

    定义k = max(|x|, |y|)
    观察发现右上角(y=x)点步数step=4k^2
    进而推出右下角4k^2+2, 左下角(y=x)4k^2+4k, 左上角4k^2-2k

    定义less = x - y
    上线以右上角为基准, 步数为4k^2 + less
    右线以右上角为基准, 步数为4k^2 + less
    下线以右下角为基准, 步数为4k^2+4k - less
    左线以左上角为基准,步数为4k^2-2k + less, 避免k变化的混淆

    使用y=x, y=-x两条对角线夹出四线范围, 对角线位置另做判断直接套78行公式
    上线y>x and y>-x
    右线y<x and y>-x
    下线y<x and y<-x
    左线y>x and y<-x
"""
def dis(x, y):
    k = max(abs(x), abs(y))
    less = x - y
    # 判断是否为对角线坐标
    if x == y:
        if x >= 0:
            # 右上角
            return 4*k*k
        else:
            # 左下角
            return 4*k*k + 4*k
    elif x == -y:
        if y >= 0:
            # 左上角
            return 4*k*k - 2*k
        else:
            # 右下角
            return 4*k*k + 2*k

    # 判断位于哪条线,以角点为基准推距离
    if y > x:
        if y > -x:
            # 上线
            return 4*k*k + less
        else:
            # 左线
            return 4*k*k - 2*k + less
    if y < x:
        if y > -x:
            # 右线
            return 4*k*k + less
        else:
            # 下线
            return 4*k*k - less

x, y = map(int, input().split())
print(dis(x, y))
# 以上大数据WA......
# 不知道有什么问题
"""
对角线y=x定位加曼哈顿距离计算
    接收x y 后取得 k = max(|x|, |y|)
    寻找k, k位置(右上角)作为基准, step=4k*k
    对角线及以下增加曼哈顿距离
    对角线以上减去曼哈顿距离
"""
def md(x, y, k):
    return abs(k - x) + abs(k - y)
def dis(x, y):
    k = max(abs(x), abs(y))
    if y > x:
        return 4 * k * k - md(x, y, k)
    else:
        return 4 * k * k + md(x, y, k)
x, y = map(int, input().split())
print(dis(x, y))
# Accepted!