"""3/2/26
对于目标长度x会有类似如下满足关系
T T T T T T T F F F F
当x较小时都可以满足, x越大越不容易满足条件 counts >= m
满足条件就继续增大x向右找
另外注意本题是浮点二分
"""
n, m = map(int, input().split())
li = list(map(int, input().split()))

def count(li, x, n):
    counts = 0
    for _ in range(n):
        counts += int(li[_] // x)
    
    return counts

# 右边界取最长绳子
left, right = 0.0, max(li)
# 精度设定要高于题目要求的两位小数
eps = 1e-3
while right - left > eps:
    mid = (left + right) / 2
    counts = count(li, mid, n)
    if counts >= m:
        left = mid
    else:
        right = mid

print(f"{right:.2f}")