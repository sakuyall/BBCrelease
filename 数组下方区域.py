"""1/2/26
绿色部分可以看作满足: j<i, j>11-i的环绕部分(有些二重积分看面积的感觉)
遍历满足条件的元素并求和total, 共30格
s输出total, m输出total/30
"""
def calculate(martixx, obj):
    total = 0
    for i in range(7, 12):
        for j in range(11):
            if 11-i < j < i:
                total += martixx[i][j]
    if obj == "S":
        return total
    elif obj == "M":
        return total / 30

def main():
    martixx = []  
    obj = str(input())
    martixx = [list(map(float, input().split(" "))) for _ in range(12)]
    answer = calculate(martixx, obj)
    print(f"{answer:.1f}")

if __name__ == "__main__":
    main()