"""3/13/26
分为k组至少为1
两数绝对值最大值差小于等于5
数要多

实际上是没有完成的题目, 贪心并不是最优解
但此题限时内做完并满足给定样例已经够了
应使用动态规划, 放在后边学习
今天复习了前两天的题目, 但是效果不是很好
"""
#------------------------------------------------------------
# 数据处理
n, k = map(int, input().split())
li = list(map(int, input().split()))

if n < 2:
    print(1)
    exit()

# 原地排序
li.sort()
i, counts, flag = 0, 0, 0
while i < n:
    j = i + 1
    while j < n and abs(li[j] - li[i]) <= 5:
        j += 1

    # 记录该组长度并开始寻找下一组数， 组数加1
    flag += 1
    counts += j - i
    i = j
    
    if flag == k:
        # 数目达到设定组数停止寻找
        print(counts)
        break