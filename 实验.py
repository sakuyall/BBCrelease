"""1/6/26
使用字典储存计数并进行后续输出
给定输出里边百分号前有个空格, 使用格式化.2%没有, 会发生Presentation Error……
\n后边的续行符\是观感上用来换行的不会输出
"""
def stat(num, typ, dic):
    dic[typ] += num        # 对应值累加
    return dic

n = int(input())
dic = {"C": 0, "R": 0, "F": 0}
for _ in range(n):
    num, typ = input().split()
    num = int(num)
    dic = stat(num, typ, dic)    # 每次循环更新字典

total = sum(dic.values())
totalc = dic.get("C")
totalr = dic.get("R")
totalf =  dic.get("F")

print(f"Total: {total} animals\n\
Total coneys: {totalc}\n\
Total rats: {totalr}\n\
Total frogs: {totalf}\n\
Percentage of coneys: {totalc*100 / total:.2f} %\n\
Percentage of rats: {totalr*100 / total:.2f} %\n\
Percentage of frogs: {totalf*100 / total:.2f} %")