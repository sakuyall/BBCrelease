"""1/3/26
注意使用.splitlines()不会等待多行输入, 它用于将一个多行字符串分割
"""
li = [int(input()) for _ in range(20)]
reli = li[::-1]
for _ in range(20):
    print(f"N[{_}] = {reli[_]}")