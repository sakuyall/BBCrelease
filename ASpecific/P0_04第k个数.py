"""1/19/26
样例234两行三列矩阵为:
1 2 3    ---->   1 2 2 3 4 6     ---->  返回3(x)    找出序列中第k个数
2 4 6    排列          ↑取第4个(k)                  该数与ij有关, 满足以下条件
                                                    对ij进行判断, 统计有多少数满足条件
                                                            |
设排序出来第k个数为x                                        V
也就是对于给定的x, 有多少对(i, j)满足1 <= i <= n, 1 <= j <= m且i * j <= x
i的范围为[1, n], j的满足个数min(m, x//i)-->因为是从1开始编号, x整除行编号i就可以得到列编号(向下取)
所以总个数counts为遍历i范围, 满足条件j个数的加和

如果第 k 个数 = x，x越大, counts越大, 单调不减
满足 count(x) ≥ k 且 count(x-1) < k的边界条件, 可以不断增大x使counts贴近k
x范围[1, n * m], 分别为矩阵左上角与右下角元素
找第一个counts >= k的
"""
def count(n, m, x):
    counts = 0
    for i in range(1, n+1):                 # 从1开始编号
        counts += min(m, x // i)
        
    return counts

n, m, k = map(int, input().split())         # 行 列 第k个数
left, right = 1, n * m         # x边界
ans = left                     # 初值

while left <= right:
    mid = (left + right) // 2
    counts = count(n, m, mid)
    if counts >= k:
        ans = mid              # 记录
        right = mid - 1        # x需要更小, 向左半找
    else:
        left = mid + 1         # x过小, 向右找

print(ans)