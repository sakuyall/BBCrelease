"""12/1/25
分核桃问题
    设核桃为n
    n必须能被a b c 整除
    所以n是它们的最小公倍数
    lcm(a,b) = a * b / 最大公约数gcd(a,b)
"""
import math

def main():
    a, b, c = map(int, input().split())
    # 分别求最小公倍数即可
    lcm_ab = a * b // math.gcd(a, b)
    lcm_abc = lcm_ab * c // math.gcd(lcm_ab, c)
    print(lcm_abc)

if __name__ == "__main__":
    main()
# 只有当这个文件被直接运行时，才调用 main() 函数；如果被其他文件导入，不会自动执行。
