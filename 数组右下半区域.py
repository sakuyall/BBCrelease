"""11//25
和另一道下部分数组差不多
"""
def calculate(li, cap):
    sum = 0
    for i in range(12):
        for j in range(12):
            if 11-i < j < 12:
                sum += li[i][j]
    if cap == "S":
        return sum
    return sum / 66
    
def main():
    cap = input()
    martixx = [list(map(float, input().split())) for _ in range(12)]
    answer = calculate(martixx, cap)
    print(f"{answer:.1f}")

if __name__ == "__main__":
    main()