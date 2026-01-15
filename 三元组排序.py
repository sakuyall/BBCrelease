"""1/15/26
生成器表达式占用内存会多于直接for循环遍历
"""
n = int(input())
li = []
for _ in range(n):
    x, y, z = input().split()
    li.append((int(x), float(y), str(z)))  # 输入后立即转换为正确类型

li_s = sorted(li, key = lambda x: x[0])
for x, y, z in li_s:
    print(f"{x} {y:.2f} {z}")
    
# 或者这个for循环可以写成生成器表达式
# print("\n".join(f"{x} {y:.2f} {z}" for x, y, z in li_s))