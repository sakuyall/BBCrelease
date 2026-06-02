'''6/2/26
树状数组
'''
tree = []
n = 0

def lowbit(x):
    return x & -x

def init(size):
    global tree, n
    n = size
    tree = [0] * (n + 1)

def add(x, v):
    while x <= n:
        tree[x] += v
        x += lowbit(x)

def query(x):
    res = 0
    while x > 0:
        res += tree[x]
        x -= lowbit[x]
    return res

def range_query(l, r):
    return query(r) - query(l - 1)
