"""3/12/26
已给两组数据总和相同
核心目标就是通过合并操作
在保证两人最终石子堆数相同且对应堆石子数相等的前提下
尽可能多地保留堆数
"""
# 数据处理
n, m = map(int, input().split())
la = list(map(int, input().split()))
lb = list(map(int, input().split()))

# 初始化, 由于题中说至少有一堆, 所以从第一堆开始计数
i, j, k = 1, 1, 1
sum_a, sum_b = la[0], lb[0]
while i < len(la) and j < len(lb):
    if sum_a < sum_b:
        sum_a += la[i]
        i += 1

    elif sum_a > sum_b:
        sum_b += lb[j]
        j += 1

    else:
        k += 1
        # 开始新的一段
        if i < len(la) and j < len(lb):
            # 注意初始采用了ij为1, 总指向下一个数, 所以先重置sum再前进ij
            sum_a = la[i]
            sum_b = lb[j]
            i += 1
            j += 1


print(k)