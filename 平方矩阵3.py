"""1/14/26
矩阵每一个位置martixx[i][j]的值为2的(i+j)次幂
ij调换位置直接镜像赋值, 所以循环范围限定为下三角矩阵部分
"""
while True:
    n = int(input())
    if n == 0:                         # 读取到0直接结束
        break
    
    martixx = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i+1):
            value = 1 << (i + j)       # 位运算
            # value = pow(2, i+j)      # 调用函数
            # value = 2 ** (i+j)       # 幂运算
            martixx[i][j] = value
            martixx[j][i] = value
    
    for row in martixx:
        print(*row)
    print()                            # 结尾一个空行

# 列表推导式简化
while True:
    n = int(input())
    if n == 0:
        break
    
    # 一行生成整个矩阵
    matrix = [[1 << (i+j) for j in range(n)] for i in range(n)]
    
    for row in matrix:
        print(*row)
    print()