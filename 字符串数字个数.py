"""1/5/26
"""
s = input()
count = 0
for i in s:
    if i.isdigit():   # 挨个判断是否为数字, 是就加1
        count += 1
print(count)