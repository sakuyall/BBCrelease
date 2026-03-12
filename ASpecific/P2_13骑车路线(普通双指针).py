"""3/12/26
两个及以上连续单调不减为爬坡, 高度差为该子序列结尾减开头
寻找爬坡序列, 不断更新高度差
"""
import sys

while True:
    # 数据处理
    line = sys.stdin.readline()
    if not line:
        break
    line = line.strip()
    if not line:
        continue
    
    n = int(line)
    # 读取海拔数据
    parts = sys.stdin.readline().strip()
    li = list(map(int, parts.split()))

    i, vertigo = 0, 0
    while i < n - 1:
        if li[i] < li[i + 1]:
            lower = li[i]
            j = i + 1
            
            while j < n - 1 and li[j] <= li[j + 1]:
                # 单调不减持续前进, 下一个不满足就停止
                j += 1
            higher = li[j]
            vertigo = max(vertigo, higher - lower)

            # i移动到爬坡终点后
            i = j + 1
            
        else:
            i += 1
            
    print(vertigo)
