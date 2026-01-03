"""1/3/26
获取ASCII码ord(), 反向操作chr()
"""
a = input()
n = len(a)
b = ""
for i in range(n):
    b += chr(ord(a[i]) + ord(a[(i + 1) % n]))  # 正确拼接
print(b)