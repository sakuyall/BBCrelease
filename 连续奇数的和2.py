"""1/13/26
对于x与y举例:
0到10, x偶y偶, 中间奇数个数m为(10-0) // 2 = 5
0到11, x偶y奇, 中间奇数个数m为(11-0) // 2 = 5
1到10, x奇y偶, 中间奇数个数m为(10-1) // 2 = 4
1到11, x奇y奇, 中间奇数个数m为(11-1) // 2 - 1 = 4 (这个特殊, 所以单写一个判断)

求和可以看作1+2*0 1+2*1 1+2*2 1+2*3 1+2*4, 即s*m + 2*(1+2+3+4), s为开头第一个奇数
后半部分利用数列求和写作(1+m-1)*(m-1)

得到结果为 m*(s+m-1), 其中m = (y - x) // 2
因为取值范围不包括xy, 再判断一下开头的x+1是否为奇数, 奇数直接带入s
"""
def calculate():
    x, y = map(int, input().split())
    if x > y:                      # 假如x更大, 修改边界顺序
        x, y = y, x

    if x % 2 == 1 and y % 2 == 1:  # 对应前边推的x奇y奇条件判断
        m = ((y - x) // 2) - 1
    else:
        m = ((y - x) // 2)

    if m <= 0:                     # 解决两数相同时候的问题
        print(0)
        return

    if x % 2 == 0:                 # 确定第一个奇数
        s = x + 1
    else:
        s = x + 2

    print(m*(s+m-1))

n = int(input())
for _ in range(n):
    calculate()

# 暴力
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())

    if x > y:
        x, y = y, x          # 假如x更大, 修改边界顺序

    total = 0
    for i in range(x + 1, y):
        if i % 2 != 0:       # 如果是奇数就加
            total += i
    print(total)