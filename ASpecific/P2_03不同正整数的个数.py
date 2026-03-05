"""3/5/26
初始两个指针ij都位于开头
遇到0或者重复数字j右移
"""
n = int(input())
li = list(map(int, input().split()))

# 先排序
li.sort()
count = 0
i = 0
while i < n:
    # 如果当前数是正整数
    if li[i] > 0:
        count += 1
        # 跳过后面所有相同的数
        j = i + 1
        while j < n and li[j] == li[i]:
            j += 1
        i = j
    else:
        # 如果是0，直接跳过
        i += 1

print(count)