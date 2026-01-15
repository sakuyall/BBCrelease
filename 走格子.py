"""1/15/26
往下需要走n步, 往右需要走m步
共需 n+m 步, 每步无非往下或往右两种走法

以2 3为例
实际走法排列可以看作, 2个黑球与3个白球的排列方式, 同种颜色球完全相同
走法数 = 从 5 个球中选择 2 个位置不分先后的涂黑, 也就是C52

可以用组合数Cm+n n = (m+n)! / (m! * n!)
"""
# 刚好刚做完阶乘的题
def fact(n):
    if n == 0:
        return 1               # 0的阶乘返回1
    else:
        return n * fact(n - 1) # 返回该数与上个阶乘的乘积

n, m = map(int, input().split())
ans = fact(m+n) / fact(n) / fact(m)
print(int(ans))