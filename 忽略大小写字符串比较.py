"""1/4/26
优先比较字符串长短
接着挨个比较, 出现一方较大时直接输出>或<, 否则返回=
由于Python可以直接比较大小, 所以只要解决大小写问题即可
使用str.casefold(), 或者全部转换为.upper()大写或.lower()小写再比较

或者也可以这么写:
# 利用ab运算结果返回列表对应位置符号, 能更节省
a, b = input().casefold(), input().casefold()
print(["=", ">", "<"][(a>b)-(a<b)])
"""
def comp(a, b):
    a_cf, b_cf= a.casefold(), b.casefold()  # 只调用一次casefold(), 提高性能
    if a_cf > b_cf:
        print(">")
    elif a_cf < b_cf:
        print("<")
    else:
        print("=")

a = input()
b = input()
comp(a, b)