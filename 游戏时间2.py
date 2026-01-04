"""1/4/26
多出来一个特殊的24小时时间, 单拿出来写
"""
def countime(a, b, c, d):
    if a == c and b == d:          # 固定情况输出24小时
        print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
        return

    totalm = c * 60 + d - a * 60 -b
    if totalm < 0:
        totalm += 24 * 60
        
    X, Y = totalm // 60, totalm % 60
    print(f"O JOGO DUROU {X} HORA(S) E {Y} MINUTO(S)")
    
a, b, c, d = map(int, input().split())
countime(a, b, c, d)

# 优化后版本
