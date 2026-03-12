"""3/11/26
子序列指针
"""
t = int(input())
for _ in range(t):
    ii = str(input())    # 测试内容
    pp = str(input())    # 输出内容

    if len(pp) < len(ii):
        print(f"Case #{_+1}: IMPOSSIBLE")
        continue

    # 同步移动, 检测下一位置字符是否相同, 不同则跳过并计数
    counts, i, j = 0, 0, 0
    while i < len(ii) and j < len(pp):
        # 出现不同字符计数直到出现相同字符, i前进
        if pp[j] != ii[i]:
            counts += 1
        else:
            i += 1

        j += 1

    # 以上循环结束, 如果i没走完ii，说明pp中字符不够匹配ii
    if i < len(ii):
        print(f"Case #{_+1}: IMPOSSIBLE")
        continue

    # 如果走完了, 则pp剩余字符为多余字符, 加入counts
    counts += len(pp) - j
    print(f"Case #{_+1}: {counts}")
