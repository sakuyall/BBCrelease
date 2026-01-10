def conduct():
    n = int(input())
    if n == 0:                             # 生成矩阵前判断是否结束
        return False

    martixx = [[0] * n for _ in range(n)]  # 正确初始化列表
    for i in range((n+1)//2):              # 限定左上半范围
        for j in range((n+1)//2):
            value = min(i, j) + 1          # ij的最小值+1为该位置数值

            martixx[i][j] = value          # 赋值与镜像
            martixx[i][n-1-j] = value
            martixx[n-1-i][j] = value
            martixx[n-1-i][n-1-j] = value

    return martixx             # 因为多次输入所以做个函数清晰些

def print_m(ans):              # 自定义矩阵打印
    for row in ans:
        print(' '.join(str(x) for x in row))
        # str(x) for x in row返回的是一个迭代器, 所以可以为.join()操作

while True:
    ans = conduct()
    if not ans:                # 检测返回为0退出循环, 这一过程不用输出空行
        break
    print_m(ans)
    print()                    # 结尾再输出一个空行