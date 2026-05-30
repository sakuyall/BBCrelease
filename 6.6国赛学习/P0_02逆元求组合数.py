'''5/30/26
学了很长时间了, 整理一下
对于要求大数取模的问题, 以前的comb函数显得力不从心
采用逆元与阶乘预处理方法重写
注意求阶乘的过程中也随时取模
'''
def inv(x):
    return pow(x, mod - 2, mod)

def comb(n, m):
    # 注意是这两个特判
    if n < m or m < 0:
        return 0

    return fac[n] * inv(fac[n - m]) % mod * inv(fac[m]) % mod
    
# 阶乘预处理
end = 100
mod = 10 ** 9 + 7
fac = [1] * (end + 1)
for _ in range(1, end + 1):
    fac[_] = fac[_ - 1] * _ % mod

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(comb(n, m))# 这里也可以再取一次模
