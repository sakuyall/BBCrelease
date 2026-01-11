"""1/11/26
输入行数n, 列数m
第m列, 也就是j = m-1位置的值, 对于任意i都是"PUM", 也可看作每行结尾的元素替换
接着建立矩阵
对于每个位置的数martixx[i][j]的值可以表示为i * m + j + 1(因为元素从1开始)
最后打印
"""
def print_m(li):                              # 转换与打印
    for row in li:
        row[-1] = "PUM"                       # 每行结尾元素替换
        print(" ".join(str(x) for x in row))  # 因为里边有字符串, 所以数字也顺便换成字符串了

n, m = map(int, input().split())
# martixx = [[0 for j in range(m)] for i in range(n)]
# 这是建立0矩阵的方法, 在此推导式上修改元素赋值的内容可以得到:
martixx = [[i * m + j + 1 for j in range(m)] for i in range(n)]
print_m(martixx)

"""
超级压缩
直接限定矩阵形成范围不包括最后一列, 数值计算过程正常
在输出一行之后, 在结尾人为加上"PUM"
"""
n, m = map(int, input().split())
for i in range(n):
    print(" ".join(str(i * m + j + 1) for j in range(m - 1)), "PUM")