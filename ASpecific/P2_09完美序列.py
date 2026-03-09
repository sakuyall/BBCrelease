"""3/9/26
从给出的序列中挑出若干个数, 让它们满足题中条件
所以可以对原序列排序, 每次固定一个最小值
找出小于满足条件的数, 计算其子序列长度
通过不同的最小值, 获得多个长度, 最后取最大

但一个一个遍历最小值太慢了, 可以采用滑动窗口记录
"""
n, p = map(int, input().split())
li = list(map(int, input().split()))
li.sort()    # 原地排序

j, ans = 0, 1
for i in range(n):
    while j < n and li[j] <= li[i] * p:
        # 有序列表就好操作了不少, 满足条件持续右扩
        j += 1
    ans = max(ans, j - i)

print(ans)