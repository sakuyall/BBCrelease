"""3/10/26
快慢指针
"""
import sys

target = "EASY"
for line in sys.stdin:
    # 获取每一行输入
    s = str(line.strip())

    if not s:
        continue

    flag = 0
    for ch in s:
        if flag < 4 and ch == target[flag]:
            flag += 1

    if flag == 4:
        print("easy")
    else:
        print("difficult")
